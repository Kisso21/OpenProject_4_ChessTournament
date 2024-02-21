class Player:

    def __init__(self, firstName, lastName, dateBirth, nationalId):
        self.firstName = firstName
        self.lastName = lastName
        self.dateBirth = dateBirth
        self.nationalId = nationalId

    # Serialized information joueurs
    def format_player_save(self):
        player_formated = {"Nom": self.lastName,
                           "Prenom": self.firstName,
                           "Date de Naissance": self.dateBirth,
                           "Id": self.nationalId}
        return player_formated

    def __str__(self):
        return f"{self.lastName}"
