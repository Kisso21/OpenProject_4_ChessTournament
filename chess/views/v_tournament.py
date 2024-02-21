from models.m_tournament import Tournament
from control.c_database import DatabaseTournament
import json


class ViewTournament:

    # Affichage de tous les tours et les matchs d'un tournoi
    def display_list_rounds_match_tournament(self):
        tournamentList = ViewTournament().display_list_tournament()
        reponse = input("Quels tournois veux tu ? (entre le nom):")
        for tournament in tournamentList:
            if reponse == tournament["Nom"]:
                print(
                    f"TOURNAMENT: {tournament["Nom"]}  "
                    f"DEBUT: {tournament["Date de debut"]} "
                    f"FIN: {tournament["Date de fin"]}")
                for round, infoRound in tournament["Tour"].items():
                    print(round)
                    for match in infoRound["Match"]:
                        print(match)

    # Affichage de tous les joueurs dans un tournoi
    def display_list_players_tournament(self):
        tournamentList = ViewTournament().display_list_tournament()
        reponse = input("Quels tournois veux tu ? (entre le nom):")
        for tournament in tournamentList:
            if reponse == tournament["Nom"]:
                listSortedPlayers = sorted(tournament["Liste participants"], key=lambda joueur: joueur['Nom'],
                                           reverse=False)
                for player in listSortedPlayers:
                    print(f"{player["Nom"]} {player["Prenom"]}")

    # Affichage de tous les tournois
    def display_list_tournament(self):
        try:
            with open("BDDTournament.json", "r") as json_file:
                infoTemp = json.load(json_file)
                # Vérifier si la liste de tournois est vide ou non
                if not infoTemp:
                    print("Aucun tournois dans la base")
                else:
                    for tourna in infoTemp:
                        print(f"{tourna["Nom"]} - {tourna["Date de debut"]}")
                return infoTemp
        except json.decoder.JSONDecodeError:
            print("Format de fichier invalide")
        except FileNotFoundError:
            print("Aucun fichier trouvé")

    # Affichage pour la création d'un tournoi
    def display_creation_tournament(self):
        name = input("\033[1;32mNom du tournoi: \033[0m")
        location = input("\033[1;32mLieu: \033[0m")
        while True:
            nb_turn = input("\033[1;32mVeuillez entrer le nombre de tours : \033[0m")
            if nb_turn.isdigit():
                nb_turn = int(nb_turn)
                break
            else:
                print("\033[1;31mVeuillez choisir un vrai chiffre\033[0m")
        tournament = Tournament(name, location, nb_turn)
        return tournament

    # Affichage des points de chaques participants
    def display_players_points(self, tournament):
        print("\033[1;34m-- LISTE DES PARTICIPANT --\033[0m\n")
        for i in tournament.players_points:
            print(f"PRENOM:{i["Nom"]}\tNOM:{i["Prenom"]}\tPOINTS:{i["Points"]}\n")

    # Affichage de tous les joueurs et leurs informations
    def display_player_in_tournament(self, tournament):
        print("\033[1;34m-- LISTE DES PARTICIPANT --\033[0m\n")
        for i in tournament.player_selected:
            print(f"PRENOM:{i["Nom"]}\tNOM:{i["Prenom"]}\tDATE DE NAISSANCE:{i["Date de Naissance"]}\tID:{i["Id"]}\n")

    # Affichage pour importer un joueur
    def display_importation_player(self):
        playerFind = False
        with open("BDDplayer.json", "r") as json_file:
            infoTemp = json.load(json_file)
            list_sorted = sorted(infoTemp, key=lambda x: x["Nom"])
            for joueur in list_sorted:
                print(joueur)
        reponse = input("Selectioner l'id a importer dans le tournois :")
        for joueur in infoTemp:
            if joueur["Id"] == reponse:
                return joueur
                break
            else:
                playerFind = True
        if playerFind:
            print("\033[1;31mJoueur non trouvé\033[0m")

    # Affichage pour charger un tournoi
    def display_tournament_loading(self):
        list_tournament = DatabaseTournament().CheckTournament()
        if not list_tournament:
            pass
        else:
            print("\033[1;34m--- LISTE TOURNOIS ---\033[0m\n")
            for tournament in list_tournament:
                print(f"{tournament["Nom"]} - {tournament["Date de debut"]}\n")
            reponse = input("Entrez le nom exact du tournois à charger :")
            for tournament in list_tournament:
                if tournament["Nom"] == reponse:
                    LoadTournament = Tournament(tournament["Nom"],
                                                tournament["Location"],
                                                start_date=tournament["Date de debut"],
                                                nb_turn=tournament["Nombre de rounds"],
                                                turn_actually=tournament["Tour actuel"],
                                                list_turn=tournament["Tour"],
                                                player_selected=tournament["Liste participants"],
                                                players_points=tournament["Liste points"],
                                                match_played=tournament["Match jouer"])
                    return LoadTournament
