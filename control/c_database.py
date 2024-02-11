import json


class DatabasePlayer:

    # Ajout d'un joueur dans le fichier JSON des joueurs
    def AddPlayer(self, player):
        new_player = player.format_player_save()
        try:
            with open("BDDplayer.json", "r") as json_file:
                infoTemp = json.load(json_file)
                infoTemp.append(new_player)
            with open("BDDplayer.json", "w") as json_file:
                json.dump(infoTemp, json_file, indent=2)
        except json.decoder.JSONDecodeError:
            with open("BDDplayer.json", "w") as json_file:
                json.dump(infoTemp, json_file, indent=2)
        except FileNotFoundError:
            with open("BDDplayer.json", "w") as json_file:
                pass

    # Suppression d'un joueur dans le fichier JSON des joueurs
    def DeletePlayer(self, nationalId):
        compteur = 0
        playerFind = False
        with open("BDDplayer.json", "r") as json_file:
            infoTemp = json.load(json_file)
            for player in infoTemp:
                if player["Id"] == nationalId:
                    del infoTemp[compteur]
                    playerFind = True
                    break
                else:
                    compteur += 1
        if not playerFind:
            print("\033[1;31mJoueur non trouvé\033[0m")
        with open("BDDplayer.json", "w") as json_file:
            json.dump(infoTemp, json_file, indent=2)

    # Affichage des joueurs dans la database JSON
    def CheckPLayer(self):
        try:
            with open("BDDplayer.json", "r") as json_file:
                infoTemp = json.load(json_file)
                for joueur in infoTemp:
                    print(f"PRENOM:{joueur["Prenom"]}\t"
                          f"NOM:{joueur["Nom"]}\t"
                          f"DATE DE NAISSANCE:{joueur["Date de Naissance"]}\t"
                          f"ID:{joueur["Id"]}\n")
        except json.decoder.JSONDecodeError:
            print("\033[1;31mFichier DATABASE VIDE\033[0m")


class DatabaseTournament:

    # Ajout / save d'un tournoi dans la base de donnée JSON
    def AddTournament(self, tournament):
        save = tournament.format_tournament_save()
        try:
            with open("BDDTournament.json", "r") as json_file:
                infoTemp = json.load(json_file)
                # Vérifier si la liste de tournois est vide ou non
            if not infoTemp:
                infoTemp.append(save)
            else:
                tournoi_existe = False
                # Parcourir la liste des tournois existants
                for t in infoTemp:
                    if t["Nom"] == save["Nom"]:
                        # Mettre à jour les informations du tournoi existant
                        t["Location"] = save["Location"]
                        t["Date de debut"] = save["Date de debut"]
                        t["Date de fin"] = save["Date de fin"]
                        t["Nombre de rounds"] = save["Nombre de rounds"]
                        t["Tour actuel"] = save["Tour actuel"]
                        t["Tour"] = save["Tour"]
                        t["Liste participants"] = save["Liste participants"]
                        t["Liste points"] = save["Liste points"]
                        t["Match jouer"] = save["Match jouer"]
                        t["Description"] = save["Description"]
                        tournoi_existe = True
                        break

                # Si le tournoi n'existe pas encore, l'ajouter à la liste
                if not tournoi_existe:
                    infoTemp.append(save)
            with open("BDDTournament.json", "w") as json_file:
                json.dump(infoTemp, json_file, indent=2)
        except json.decoder.JSONDecodeError:
            with open("BDDTournament.json", "w") as json_file:
                json.dump(save, json_file, indent=2)
        except FileNotFoundError:
            with open("BDDTournament.json", "w") as json_file:
                print("\033[1;31mFichier DATABASE NON TROUVE\033[0m")
                pass

    # Méthode pour voir les tournois non terminés
    def CheckTournament(self):
        list_tournament = []
        try:
            with open("BDDTournament.json", "r") as json_file:
                infoTemp = json.load(json_file)
                # Vérifier si la liste de tournois est vide ou non
            if not infoTemp:
                print("\033[1;31mFichier DATABASE VIDE\033[0m")
            else:
                # Parcourir la liste des tournois existants non terminés
                for t in infoTemp:
                    if t["Tour actuel"] == t["Nombre de rounds"] + 1:
                        print("Aucun tournois non terminé trouvé")
                        pass
                    else:
                        list_tournament.append(t)
                return list_tournament
        except FileNotFoundError:
            with open("BDDTournament.json", "w") as json_file:
                pass
        except json.decoder.JSONDecodeError:
            print("\033[1;31mFichier DATABASE VIDE\033[0m")
