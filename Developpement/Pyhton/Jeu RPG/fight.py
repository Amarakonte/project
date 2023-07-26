from pickle import dump
from random import randint,choice
import character
import game
import map

class fight:
    global nbr
    nbr = 0
    global Fight
    Fight = True
    
    def fight_interface(Attacker,Enemy):
        if Attacker.pv < 0:
            Attacker.pv = 0
        if Enemy.pv < 0:
            Enemy.pv = 0
        print("\n--",Attacker.name,"--\nPV :",Attacker.pv,"\nMana :",Attacker.mana)
        print("--",Enemy.name,"--\nPV :",Enemy.pv,"\nMana :",Enemy.mana)

    def chance_of_dodging(Attacker,Enemy):
        if Attacker == game.Joueur:
            touch = (Attacker.dodge * 50)/((Attacker.dodge + Enemy.dodge)/2) + 20
        else:
            touch = (Attacker.dodge * 50)/((Attacker.dodge + Enemy.dodge)/2)
        if randint(0,100) <= touch:
            return True
        else:
            print("--",Attacker.name,"a manqué son attaque sur",Enemy.name,"! --")
            return False

    def chance_of_critical(Attacker,Enemy):
        critical = (Attacker.crit * 50)/(((Attacker.crit) + Enemy.crit)/2)
        if randint(0,100) <= critical:
            print("--",Attacker.name,"fait un coup critique ! Et inflige le double des dégâts à",Enemy.name,"! --")
            return True
        else:
            return False

    def chance_of_escape(Attacker,Enemy):
        pass

    def damage(Attacker,Enemy):
        f = open("save.txt","wb")
        A = Attacker
        E = Enemy
        touch = fight.chance_of_dodging(Attacker,Enemy)
        if touch == True:
            critical = fight.chance_of_critical(Attacker,Enemy)
            dmg = (((Attacker.level/2)+50)*Attacker.force)/((Enemy.defense*50)+50) + 50
            if critical == True:
                Enemy.pv -= round(dmg)*2
                print("--",Attacker.name,"attaque",Enemy.name,"et fait",round(dmg)*2," pts de dégâts ! --")
            else:
                Enemy.pv -= round(dmg)
                print("--",Attacker.name,"attaque",Enemy.name,"et fait",round(dmg)," pts de dégâts ! --")
            fight.fight_interface(Attacker,Enemy)
        fight.end_fight(A,E)
        global Saved
        Saved = game.Joueur
        dump(Saved,f)
        f.close()
            
    def end_fight(Attacker,Enemy):
        f = open("save.txt","wb")
        global Fight
        if Enemy.pv <= 0 and Enemy.name != game.Joueur.name :
            Fight = False
            x = choice(Enemy.loot)
            z = x.name
            print("-- Vous avez tuer",Enemy.name,"!\nVous récupérer :",z,"--")
            character.player.add_item(x)
            Attacker.xp += Enemy.XP
            character.player.level_up(game.Joueur)
        elif Attacker.pv <= 0 and Attacker.name == game.Joueur.name:
            Fight = False
            Attacker.xp -= Attacker.max_xp*0.8
            if Attacker.xp < 0:
                Attacker.xp = 0
            print("-- Vous êtes mort ! --")
            game.Joueur.location_name = "La Capitale"
            game.Joueur.locationID = 0
            game.Joueur.pv = game.Joueur.pv_max
            game.Joueur.mana = game.Joueur.mana_max
            map.PosX = 0
            map.PosY = 0
            input("Vous réssuciter dans \'La Capitale\'")
        elif Enemy.pv <= 0 and Enemy.name == game.Joueur.name :
            Fight = False
            Enemy.xp -= Enemy.max_xp*0.8
            if Enemy.xp < 0:
                Enemy.xp = 0
            print("-- Vous êtes mort ! --")
            game.Joueur.location_name = "La Capitale"
            game.Joueur.locationID = 0
            game.Joueur.pv = game.Joueur.pv_max
            game.Joueur.mana = game.Joueur.mana_max
            map.PosX = 0
            map.PosY = 0
            input("Vous réssuciter dans \'La Capitale\'")
        global Saved
        Saved = game.Joueur
        dump(Saved,f)
        f.close()
            
    
