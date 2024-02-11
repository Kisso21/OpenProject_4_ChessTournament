from views.v_player import ViewCreatePlayer
from views.v_tournament import ViewTournament
from control.c_database import DatabaseTournament
from control.c_database import DatabasePlayer


class MainMenu:

    def display_main_menu(self):
        while True:
            print("\n")
            print("\033[1;34m--- Menu principal ---\033[0m")
            print("\n")
            print("1 - Menu joueurs")
            print("2 - Menu tournois")
            print("3 - Menu Rapport")
            print("4 - Sortir")
            print("\n")
            reponse = input("Quel est ton choix ? ")
            print("\n")
            match reponse:
                case "1":
                    MainMenu().display_player_menu()
                case "2":
                    MainMenu().display_tournament_menu()
                case "3":
                    MainMenu().display_rapport_menu()
                case "4":
                    quit()
                case _:
                    print("\033[1;31mVeuillez choisir une option possible\033[0m")

    def display_player_menu(self):
        while True:
            print("\n")
            print("\033[1;34m--- Menu Joueurs ---\033[0m")
            print("\n")
            print("1 - Créer un joueur")
            print("2 - Voir les joueurs existants")
            print("3 - Supprimer joueurs")
            print("4 - Retour")
            print("\n")
            reponse = input("Quel est ton choix ? ")
            print("\n")
            match reponse:
                case "1":
                    ViewCreatePlayer().display_create_player()
                case "2":
                    DatabasePlayer().CheckPLayer()
                case "3":
                    ViewCreatePlayer().delete_player()
                case "4":
                    MainMenu().display_main_menu()
                case _:
                    print("\033[1;31mVeuillez choisir une option possible\033[0m")

    def display_tournament_menu(self):
        while True:
            print("\n")
            print("\033[1;34m--- Menu tournois ---\033[0m")
            print("\n")
            print("1 - Créer un tournoi")
            print("2 - Charger un tournoi")
            print("3 - Retour")
            print("\n")
            reponse = input("Quel est ton choix ? ")
            print("\n")
            match reponse:
                case "1":
                    tournament = ViewTournament().display_creation_tournament()
                    MainMenu().display_setting_tournament_menu(tournament)
                case "2":
                    LoadingTournament = ViewTournament().display_tournament_loading()
                    if not LoadingTournament:
                        MainMenu().display_tournament_menu()
                        print("\033[1;31mTournois non trouvé\033[0m")
                    else:
                        MainMenu().display_active_tournament_menu(LoadingTournament)

                case "3":
                    MainMenu().display_main_menu()
                case _:
                    print("\033[1;31mVeuillez choisir une option possible\033[0m")

    def display_setting_tournament_menu(self, tournament):
        while True:
            print("\n")
            print(f"\033[1;34m--- TOURNOI: {tournament.name} ---\033[0m")
            print("\n")
            print("1 - Ajouter joueur")
            print("2 - Voir joueurs inscrit")
            print("3 - Importer joueurs")
            print("4 - Lancer le tournoi")
            print("5 - Menu principal")
            print("\n")
            reponse = input("Quel est ton choix ? ")
            print("\n")
            match reponse:
                case "1":
                    player = ViewCreatePlayer().display_create_player()
                    tournament.player_selected.append(player.format_player_save())
                case "2":
                    ViewTournament().display_player_in_tournament(tournament)
                case "3":
                    result = ViewTournament().display_importation_player()
                    if result:
                        tournament.player_selected.append(result)
                        print(f"\033[1;32mJoueurs importé : \033[0m {result["Nom"]} {result["Prenom"]}")
                case "4":
                    MainMenu().display_active_tournament_menu(tournament)
                case "5":
                    MainMenu().display_main_menu()
                case _:
                    print("\033[1;31mVeuillez choisir une option possible\033[0m")

    def display_active_tournament_menu(self, tournament):

        if tournament.turn_actually == 1:
            tournament.creation_players_points()
            tournament.creation_turn()
        print("\n")
        print(f"\033[1;34mTOURNOI: {tournament.name} Lieu: {tournament.location}\033[0m\n")
        while tournament.turn_actually < int(tournament.nb_turn) + 1:
            print(f"\n\t\033[1;94mROUND {tournament.turn_actually}\033[0m\n")
            print("1 - Commencer")
            print("2 - Sauvegarder")
            print("3 - Voir les scores actuelles")
            print("4 - Retour au menu + Save tournoi")
            print("\n")
            reponse = input("Quel est ton choix ? ")
            match reponse:
                case "1":
                    tournament.CreateMatch()
                    tournament.turn_actually += 1
                case "2":
                    DatabaseTournament().AddTournament(tournament)
                case "3":
                    ViewTournament().display_players_points(tournament)
                case "4":
                    DatabaseTournament().AddTournament(tournament)
                    MainMenu().display_main_menu()
                case _:
                    print("\033[1;31mVeuillez choisir une option possible\033[0m")
        tournament.tournament_end()
        DatabaseTournament().AddTournament(tournament)
        MainMenu().display_main_menu()

    def display_rapport_menu(self):
        while True:
            print("\n")
            print("\033[1;34m--- Menu rapports ---\033[0m")
            print("\n")
            print("1 - Rapport de tous les joueurs")
            print("2 - Rapport liste tournois")
            print("3 - Rapport des joueurs d'un tournoi par ordre alphabétique")
            print("4 - Rapport de tous les matchs des tours d'un tournoi")
            print("5 - Retour")
            print("\n")
            reponse = input("Quel est ton choix ? ")
            print("\n")
            match reponse:
                case "1":
                    DatabasePlayer().CheckPLayer()
                case "2":
                    ViewTournament().display_list_tournament()
                case "3":
                    ViewTournament().display_list_players_tournament()
                case "4":
                    ViewTournament().display_list_rounds_match_tournament()
                case "5":
                    MainMenu().display_main_menu()
                case _:
                    print("\033[1;31mVeuillez choisir une option possible\033[0m")
