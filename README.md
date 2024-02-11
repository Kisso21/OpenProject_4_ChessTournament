
# OpenClassrooms: Projet 4: Chess Tournament
Il s'agit d'un gestionnaire de tournois d'échecs.
## Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/FlorianMgs/OC_P4_ChessTournament.git
```
Placez vous dans le dossier OC_P4_ChessTournament, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```

## Utilisation
Le menu principal est divisé en 3 options.
### 1) Menu joueurs : 3 options
1 - Créer un joueur : Ajoute un nouveau joueur dans la base de donnée (BDDplayer.json)
2 - Voir les joueurs existants : Liste l'intégralité de joueurs présent dans votre base de donnée (BDDplayer.json)
3 - Supprimer joueurs : Supprime un joueurs de votre base de donnée (BDDplayer.json)

### 2) Menu tournois : 2 options
1 - Créer un tournoi : laissez vous guider par le programme pour définir le nom , le lieu et le nombre de rounds du tournoi, une fois créer vous aurez la possibilité d'ajouter un joueur , d'importer un joueur , voir les joueurs inscrits , une fois que la configuration du tournoi est bonne vous pouvez lancer le tournoi
Tournoi lancé : A chaque tour (Round) vous aurez la possibilité de lancer le round , sauvegarder le tournoi ou quitter le tournoi en sauvegardant le tournoi actuel.

2 - Charger un tournoi : Le programme permet de charger un tournoi (non terminé) des différents tournoi sauvegarder dans BDDTournament.json

### 3) Menu rapport
1 - Rapport de tous les joueurs : Liste l'intégralité de joueurs présent dans votre base de donnée (BDDplayer.json)
2 - Rapport liste tournois : Liste l'intégralité des tournois présent dans votre base de donnée (BDDTournament.json)
3 - Rapport des joueurs d'un tournoi par ordre alphabétique : Liste les joueurs d'un tournoi donné par ordre alphabétique
4 - Rapport de tous les matchs des tours d'un tournoi : Liste l'intégralité des matchs des différents tours d'un tournoi donné

### 5) Générer le rapport Flake8
- Installez flake8 avec la commande: 
```
pip intall flake8-html
```
- Tapez la commande:
```
flake8 --max-line-length=119 --format=html --htmldir=flake-report
```
- Le rapport sera généré dans le dossier flake8.

