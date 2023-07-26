import game, character, map
from pickle import *

def main():       
    menu = int(input("MAIN MENU :\n1- Create New Game \n2- Load Saved Game \n3- About \n4- Exit\n"))
    if menu == 1:
        game.game.create_new_game()
        map.move_animation()
        in_game()
    elif menu == 2:
        try:
            game.game.load_saved_game()
            in_game()
        except:
            print("Vous n'aviez pas de sauvegarde")
    elif menu == 3:
        game.game.about()
    elif menu == 4:
        game.game.exit()

def in_game():
    print("move = Se deplacer dans la carte |  use = Utiliser un objet |  pro = Afficher le profile")
    print(" inv = Afficher l'inventaire     | take = Equiper un objet  | menu = Retourner au menu principale")
    action = input("-- Que voulez-vous faire ? --\n")
    while action.lower() != "exit":
        f = open("save.txt","wb")
        if action.lower() == "help":
            print("move = Se deplacer dans la carte |  use = Utiliser un objet |  pro = Afficher le profile")
            print(" inv = Afficher l'inventaire     | take = Equiper un objet  | menu = Retourner au menu principale")
        if action.lower() == "inv":
            character.player.show_inventory(game.Joueur.inventory)
        if action.lower() == "take":
            character.player.take_weapon()
        if action.lower() == "move":
            print("Appuyer sur \'Entrer\'")
            map.move_animation()
        if action.lower() == "use":
            pass
        if action.lower() == "menu":
            Saved = game.Joueur
            dump(Saved,f)
            f.close()
            main()
        if action.lower() == "pro":
            character.player.profil()
        Saved = game.Joueur
        dump(Saved,f)
        f.close()
        action = input("-- Que voulez-vous faire ? (\'help\' pour voir les commandes)--\n")
    

main()
