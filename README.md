DESCRIPTION

Cette application permet aux utilisateurs de s'inscrire à des événements, tout en offrant une interface admin pour gérer les événements et les inscriptions. Elle propose aussi une page de statistiques des inscrits par tranche d'âge.

FONCTIONNALITES

Inscription à un événement (Nom, Prénom, Email, Nombre de places, Âge des accompagnants).

Interface admin pour créer des événements et consulter les inscriptions.

Affichage des statistiques par tranche d'âge : 0-18, 18-30, 30-50, 50-65, 65+.

INSTALLATION

Clonez le répertoire :

git clone https://github.com/votre-nom-utilisateur/event-registration-app.git
cd event-registration-app

Créez un environnement virtuel et activez-le :

python -m venv venv
source venv/bin/activate  # Sur Mac/Linux
venv\Scripts\activate    # Sur Windows

Installez les dépendances :

pip install -r requirements.txt

Effectuez les migrations de la base de données :

python manage.py makemigrations
python manage.py migrate

Créez un superutilisateur pour l'admin :

python manage.py createsuperuser

Lancez le serveur :

python manage.py runserver

ACCEDEZ A L'APPLICATION :

Interface utilisateur : http://127.0.0.1:8000/

Interface admin : http://127.0.0.1:8000/admin/
