# ❤
import character
from pickle import *

class game:
    
    def create_new_game():
        f = open("save.txt","wb")
        global Joueur
        name = str(input("Choose your name :\n"))
        print("-- Welcome to Python RPG", name ,"! --")
        Joueur = int(input("Choose your class :\n1 - Warrior\n2 - Wizard\n3 - Archer\n4 - Ninja\n"))
        if Joueur == 1:
            Joueur = "Warrior"
        elif Joueur == 2:
            Joueur = "Wizard"
        elif Joueur == 3:
            Joueur = "Archer"
        elif Joueur == 4:
            Joueur = "Ninja"
        Joueur = character.player(name,Joueur)
        print("__PROFIL__\nName : ", Joueur.name , "\nClass : ",Joueur.type_aventurer, "\nLevel : " , Joueur.level , "\nPV : "  , Joueur.pv , "\nForce : " , Joueur.force , "\nDefense : " , Joueur.defense , "\nDodge : " , Joueur.dodge)
        character.player.show_inventory(Joueur.inventory)
        global Saved
        Saved = Joueur
        dump(Saved,f)
        f.close()
        return Joueur
        

    def load_saved_game():
        f = open("save.txt","rb")
        global Joueur
        Saved = load(f)
        Joueur = Saved
        f.close()
        w = Joueur.profile["weapon"]
        a = Joueur.profile["armor"]
        print("La dernière partie sauvegarder est le personnage : \"",Joueur.name,"\"")
        character.player.profil()
        print("__INVENTORY__\nVous avez",len(Joueur.inventory),"objet dans votre inventaire !\n")
    

    def about():
        pass    

    def exit():
        print("Vous avez quitté le jeu")
        return quit()
