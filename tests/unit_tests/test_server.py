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


def test_logout(client):
	response = client.get('/logout')
	assert response.status_code == 302
