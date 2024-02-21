from datetime import datetime
import random
from models.m_match import Match


class Tournament:

    def __init__(self, name, location, nb_turn=4,
                 start_date=datetime.now().strftime("%d-%m-%Y-%H:%M:%S")[:-3],
                 end_date="", turn_actually=1, list_turn={},
                 player_selected=[], players_points=[],
                 match_played=[], description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_turn = nb_turn
        self.turn_actually = turn_actually
        self.list_turn = list_turn
        self.player_selected = player_selected
        self.players_points = players_points
        self.match_played = match_played
        self.description = description

    # Méthode pour finaliser le tournoi (Classement + Ajout d'un commentaire)
    def tournament_end(self):
        self.players_points = sorted(self.players_points,
                                     key=lambda joueur: joueur['Points'],
                                     reverse=True)
        print("Félication aux joueurs voici le résultat:")
        x = 1
        for player in self.players_points:
            print(f"{x} - {player["Nom"], player["Prenom"], player["Points"]}")
            x += 1
        self.description = input("Commentaire: ")

    # Méthode d'initialisation des points de chaques joueurs dans le tournoi
    def creation_players_points(self):
        if not self.players_points:
            for player in self.player_selected:
                self.players_points.append(player.copy())
            for player in self.players_points:
                player["Points"] = 0

    # Méthode - création des informations tours
    def creation_turn(self):
        for x in range(1, self.nb_turn + 1, 1):
            self.list_turn[f"Round {x}"] = {"Debut": "",
                                            "Fin": "",
                                            "Match": []}

    # Méthode serialized pour sauvegarder format JSON
    def format_tournament_save(self):
        tournament_formated = {"Nom": self.name,
                               "Location": self.location,
                               "Date de debut": self.start_date,
                               "Date de fin": self.end_date,
                               "Nombre de rounds": self.nb_turn,
                               "Tour actuel": self.turn_actually,
                               "Liste participants": self.player_selected,
                               "Liste points": self.players_points,
                               "Match jouer": self.match_played,
                               "Tour": self.list_turn,
                               "Description": self.description}
        return tournament_formated

    # Méthode de génération de match pour chaques tours
    def CreateMatch(self):
        # Récupération de l'heure et de la date de début de tour
        hour_date = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")[:-3]
        self.list_turn[f"Round {self.turn_actually}"]["Debut"] = hour_date

        # Mélange des joueurs aléatoires + tri
        random.shuffle(self.players_points)
        self.players_points = sorted(self.players_points,
                                     key=lambda joueur: joueur['Points'],
                                     reverse=True)
        paires_tour = []

        # Génération des paires des différents matchs
        for i in range(0, len(self.players_points), 2):
            joueur1 = self.players_points[i]
            joueur2 = self.players_points[i + 1]
            paire = (joueur1, joueur2)
            tuple_inverse = (joueur2, joueur1)  # Inverse de la paire

            if paire not in self.match_played and tuple_inverse not in self.match_played:
                paires_tour.append(paire)
                self.match_played.append(paire)
            else:
                paires_tour.append(paire)
                self.match_played.append(paire)

        # Lancement des matchs du tour
        x = 1
        for match in paires_tour:
            print("\n")
            print(f"\033[1;34m--- MATCH {x} ---\033[0m")
            match_actually = Match(match[0], match[1])
            result = match_actually.startmatch()
            self.match_played.append(match)
            self.list_turn[f"Round {self.turn_actually}"]["Match"].append(result)
            x += 1
        self.list_turn[f"Round {self.turn_actually}"]["Fin"] = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")[:-3]

        # Si le tournoi est terminé récupère la date de fin de tournoi
        if self.turn_actually == 4:
            self.end_date = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")[:-3]
