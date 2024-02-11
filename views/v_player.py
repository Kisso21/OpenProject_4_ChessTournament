from models.m_player import Player
from control.c_database import DatabasePlayer


class ViewCreatePlayer:

    # Affichage pour la creation d'un joueur
    def display_create_player(self):
        first_name = input("\033[1;32mPrenom du joueur : \033[0m")
        last_name = input("\033[1;32mNom du joueur : \033[0m")
        dob = input("\033[1;32mDate de naissance: \033[0m")
        nationalId = input("\033[1;32mNumero national : \033[0m")
        new_player = Player(first_name, last_name, dob, nationalId)
        DatabasePlayer().AddPlayer(new_player)
        return new_player

    # Affichage pour la suppression d'un joueur
    def delete_player(self):
        reponse = input("Veuillez entrez l'ID du joueur à supprimer: ")
        DatabasePlayer().DeletePlayer(reponse)
