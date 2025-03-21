# Event Registration App

## Description
Cette application permet aux utilisateurs de s'inscrire à des événements, tout en offrant une interface admin pour gérer les événements et les inscriptions. Elle propose aussi une page de statistiques des inscrits par tranche d'âge.

## Fonctionnalités
- Inscription à un événement (Nom, Prénom, Email, Nombre de places, Âge des accompagnants).
- Interface admin pour créer des événements et consulter les inscriptions.
- Affichage des statistiques par tranche d'âge : 0-18, 18-30, 30-50, 50-65, 65+.

## Installation
1. Clonez le répertoire :
```bash
git clone https://github.com/votre-nom-utilisateur/event-registration-app.git
cd event-registration-app
```

2. Créez un environnement virtuel et activez-le :
```bash
python -m venv venv
source venv/bin/activate  # Sur Mac/Linux
venv\Scripts\activate    # Sur Windows
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Effectuez les migrations de la base de données :
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Créez un superutilisateur pour l'admin :
```bash
python manage.py createsuperuser
```

6. Lancez le serveur :
```bash
python manage.py runserver
```

7. Accédez à l'application :
- Interface utilisateur : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Interface admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Utilisation
- Allez dans l'admin pour créer des événements.
- Partagez le lien de la page d'inscription pour que les utilisateurs puissent s'inscrire.
- Consultez les statistiques des inscriptions par tranche d'âge ici : [http://127.0.0.1:8000/age-statistics/](http://127.0.0.1:8000/age-statistics/)

## Structure du Projet
```
event-registration-app/
├── events/
│   ├── migrations/
│   ├── templates/events/
│   │   ├── register.html
│   │   ├── age_statistics.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── event_registration_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Technologies
- Python
- Django
- SQLite (par défaut)



