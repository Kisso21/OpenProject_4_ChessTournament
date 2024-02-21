class Match:

    def __init__(self, player_one, player_two):
        self.round = round
        self.player_one = player_one
        self.player_two = player_two
        self.result = ""

    # Lancement du match
    def startmatch(self):
        while True:
            print("\n")
            print(f"\033[1;32m{self.player_one["Nom"]} {self.player_one["Prenom"]}\033[0m"
                  f" \033[1;31mVS\033[0m "
                  f"\033[1;32m{self.player_two["Nom"]} {self.player_two["Prenom"]}\033[0m\n")
            print(f"1 - {self.player_one["Nom"]} "
                  f"{self.player_one["Prenom"]} "
                  f"gagant")
            print(f"2 - {self.player_two["Nom"]} "
                  f"{self.player_two["Prenom"]} "
                  f"gagant")
            print("3 - Egalité\n")
            reponse = input("Quels est le résultats ? ")
            match reponse:
                case "1":
                    self.player_one["Points"] += 1
                    tupleMatch = {f"{self.player_one['Nom']} "
                                  f"{self.player_one['Prenom']}": 1,
                                  f"{self.player_two['Nom']} "
                                  f"{self.player_two['Prenom']}": 0}
                    break
                case "2":
                    self.player_two["Points"] += 1
                    tupleMatch = {f"{self.player_one['Nom']} "
                                  f"{self.player_one['Prenom']}": 0,
                                  f"{self.player_two['Nom']} "
                                  f"{self.player_two['Prenom']}": 1}
                    break
                case "3":
                    self.player_one["Points"] += 0.5
                    self.player_two["Points"] += 0.5
                    tupleMatch = {f"{self.player_one['Nom']} "
                                  f"{self.player_one['Prenom']}": 0.5,
                                  f"{self.player_two['Nom']} "
                                  f"{self.player_two['Prenom']}": 0.5}
                    break
                case _:
                    print("Veuillez choisir une option possible")
        return tupleMatch
