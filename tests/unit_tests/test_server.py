import server

server.clubs = [
    {
        "name":"TOP-official",
        "email":"josh@twentyonepilots.com",
        "points":"15"
    },
    {
        "name":"TOP-France",
        "email": "tyler@twentyonepilots.fr",
        "points":"4"
    }
]

server.competitions = [
	{
		"name": "Bandito",
		"date": "2020-03-27 10:00:00",
		"numberOfPlaces": "21"
	},
	{
		"name": "Takeover",
		"date": "2025-10-22 13:30:00",
		"numberOfPlaces": "13"
	},
	{
		"name": "Skeleton",
		"date": "2025-10-22 13:30:00",
		"numberOfPlaces": "5"
	}
]


def test_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200


def test_clubs_table_points(client):
	response = client.get('/clubstable')
	assert response.status_code == 200
	assert server.clubs[0]["name"] in response.data.decode()
	assert server.clubs[1]["points"] in response.data.decode()


def test_unknown_email_adress(client):
	response = client.post('/showSummary', data={"email": "unknown@fakeadress.com"})
	assert response.status_code == 200
	assert "Unknown email adress !" in response.data.decode()
	

def test_correct_email_adress(client):
	email = "josh@twentyonepilots.com"
	response = client.post('/showSummary', data={"email": email})
	assert response.status_code == 200
	assert ("Welcome, " + email) in response.data.decode()


def test_logout(client):
	response = client.get('/logout')
	assert response.status_code == 302


def test_oudated_comp(client):
	response = client.get('/book/Bandito/TOP-official')
	assert "Something went wrong-please try again" in response.data.decode()
	assert response.status_code == 200


def test_futur_comp(client):
	comp = server.competitions[1]
	response = client.get('/book/'+comp['name']+'/TOP-official')
	assert "Places available: " + comp["numberOfPlaces"] in response.data.decode()
	assert response.status_code == 200


def test_purchase_not_enough_point(client):
	comp = server.competitions[1]
	club = server.clubs[1]
	response = client.post('/purchasePlaces', data={
		"club": club['name'],
		"competition": comp['name'],
		"places": 6
		})
	assert "You don&#39;t have enough points" in response.data.decode()
	assert response.status_code == 200


def test_purchase_max_places(client):
	comp = server.competitions[1]
	club = server.clubs[0]
	response = client.post('/purchasePlaces', data={
		"club": club['name'],
		"competition": comp['name'],
		"places": 13
		})
	assert "You can only take a maximum of 12 places" in response.data.decode()
	assert response.status_code == 200


def test_purchase_max_places_available(client):
	comp = server.competitions[2]
	club = server.clubs[0]
	response = client.post('/purchasePlaces', data={
		"club": club['name'],
		"competition": comp['name'],
		"places": 7
		})
	assert "There is not enough places available for this competition." in response.data.decode()
	assert response.status_code == 200


def test_purchase_places(client):
	comp = server.competitions[1]
	club = server.clubs[0]
	response = client.post('/purchasePlaces', data={
		"club": club['name'],
		"competition": comp['name'],
		"places": 3
		})
	assert "Great-booking complete! Number of places purchased: 3" in response.data.decode()
	assert club["points"] == 15-3*3
	assert comp["numberOfPlaces"] == 13-3
	assert club[comp['name']] == 3
	assert response.status_code == 200
