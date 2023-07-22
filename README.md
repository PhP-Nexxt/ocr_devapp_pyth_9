OCR_Projet9_LitReview

Ce projet est réalisé dans le cadre de la formation OpenClassrooms Développeur d'Applications Python
Il s'agit de construire une application web avec le framework Django pour une société LitReview(Fictive)
L'application est une forme de réseau social qui offre la possibilité de demander et de poster des critiques de livres

Les fonctionnalités sont les suivantes :
Se connecter / S'inscrire 
Consulter son flux personnalisé selon ses abonnements
Publier des demandes de critique(tickets)
Publier des critiques en réponse à une demande(Ticket) 
Publier des critiques pas en réponse à une demande(Ticket)
Modifier / supprimer ses demandes(Tickets) et ses critiques
Consulter ses abonnements
Consulter ses abonnés
Rechercher un utilisateur
S'abonner / se désabonner à un autre utilisateur


Installation & lancement :

Installer Python en version 3.8.8
Lancez  un terminal et placez vous dans le dossier de votre choix puis clonez le repository:
git clone https://github.com/PhP-Nexxt/ocr_devapp_pyth_9/tree/main

Placez vous dans le dossier ocr_devapp_pyth_9, puis créez un environnement virtuel:

python -m venv env `python -m venv litreview`

Ensuite, activez-le 
Sur MacOs/Linux `source venv_litreview/bin/activate`
Sur Windows:`venv_litereview\scripts\activate.bat`

Installez ensuite les packages requis:
pip install -r requierements.txt

Puis placez vous à la racine du projet (là ou se trouve le fichier manage.py), et effectuez les migrations:
`python manage.py makemigrations`
`python manage.py migrate`

Lancer le serveur:
`python manage.py runserver`

Vous pouvez ensuite utiliser l'applicaton avec l'url `http://127.0.0.1:8000/litreview_app/login/`