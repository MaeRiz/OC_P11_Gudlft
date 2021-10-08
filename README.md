# Application de réservation de concours Güdlft

Guldft a développé une application de réservation de concours sportifs à destination des salles de sport.

Le site est créé avec le micro-framework Flask.

## Prérequis

1. Installer [Python 3](https://www.python.org/downloads/).

2. Télécharger le programme via GitHub avec la commande ci-dessous ou en téléchargeant [l'archive](https://github.com/MaeRiz/OC_P11_Gudlft/archive/refs/heads/master.zip).
```bash
git clone https://github.com/MaeRiz/OC_P11_Gudlft.git
```

3. Créer un environnement virtuel et l'activer :
```cmd
python3 -m venv env
env\Scripts\activate
```

4. installer les modules :
```cmd
pip install -r requirements.txt
```


## Utilisation
1. Lancer le serveur Flask :
```cmd
flask run
```
2. Se rendre sur l'adresse du site par défaut : [http://localhost:5000/](http://localhost:5000/)

## Tests unitaires
- Les tests unitaires sont générés et exécutés grâce au module [**pytest**](https://docs.pytest.org/) *(compris dans le fichier requirements.txt)*.
- Ils sont situés dans le dossier **tests/unit_tests/**

L'exécution des tests se fait via la commande :
```cmd
pytest
```
La génération de couverture de test se fait via la commande :
```cmd
pytest --cov=. --cov-report html
```

## Tests de performances
- Les tests de performances sont générés et exécutés grâce au module [**locust**](https://locust.io/) *(compris dans le fichier requirements.txt)*.
- Ils sont situés dans le dossier **tests/performance_tests/**

1. Lancer le serveur de test de performance :
```cmd
locust -f tests\performance_tests\locustfile.py --web-host localhost
```
2. Se rendre sur l'adresse: [html://localhost:8089/](html://localhost:8089/)
3. Choisir les options et lancer les tests.