import random,game
import fight as f
import item as i
import map

class monster:
    def __init__(ETY,name,rang,level):
        ETY.name = name
        ETY.rang = rang
        if ETY.rang == "Start":
            ETY.loot = [i.Dagger_1,i.Sword_1,i.Staff_1,i.Bow_1,i.Armor_1,i.Dress_1,i.Cape_1,i.Mask_1]
            ETY.XP = 10*level
        elif ETY.rang == "D":
            ETY.loot = [i.Dagger_5,i.Dagger_10,i.Dagger_15,i.Dagger_20,i.Bow_5,i.Bow_10,i.Bow_15,i.Bow_20,i.Sword_5,i.Sword_10,i.Sword_15,i.Sword_20,i.Staff_5,i.Staff_10,i.Staff_15,i.Staff_20,i.Armor_5,i.Armor_10,i.Armor_15,i.Armor_20,i.Mask_5,i.Mask_10,i.Mask_15,i.Mask_20,i.Dress_5,i.Dress_10,i.Dress_15,i.Dress_20,i.Cape_5,i.Cape_10,i.Cape_15,i.Cape_20]
            ETY.XP = 50*level
        elif ETY.rang == "C":
            ETY.loot = []
            ETY.XP = 150*level
        elif ETY.rang == "B":
            ETY.loot = []
            ETY.XP = 450*level
        elif ETY.rang == "A":
            ETY.loot = []
            ETY.XP = 1350*level
        elif ETY.rang == "S":
            ETY.loot = []
            ETY.XP = 4050*level
        elif ETY.rang == "SS":
            ETY.loot = []
            ETY.XP = 12150*level
        elif ETY.rang == "SSS":
            ETY.loot = []
            ETY.XP = 36450*level
        ETY.level = level
        ETY.pv = 450*level
        ETY.mana = 175*level
        ETY.force = 140*level
        ETY.defense = 105*level
        ETY.dodge = 35*level
        ETY.crit = 70*level
    
    def pop_fight():
        mob = monster.monster(map.map.danger())
        print("Vous rencontrez \'",mob.name,"\' sur votre route...")
        f.fight.fight_interface(game.Joueur,mob)
        f.Fight = True
        f.nbr = 0
        while f.Fight != False:
            if f.nbr != 0:
                input("--- Appuyer pour continuer ---")
            f.nbr += 1
            print("\nTour",f.nbr,": Appuyer sur \"Entrer\" pour continuer")
            if f.nbr%2 == 0:
                f.fight.damage(game.Joueur,mob)
                if f.Fight == False:
                    break
            else:
                f.fight.damage(mob,game.Joueur)
                if f.Fight == False:
                    break
    
    def monster(Rang_Map):
        for x in all_monster:
            if x.rang == Rang_Map:
                return x

Cafard = monster("Cafard","Start",1)
#Rang D & C
Slime = monster("Slime","D",random.randrange(5,20,5))
Loup = monster("Loup","C",random.randrange(20,40,5))
#Rang B & A
Gobelin = monster("Gobelin","B",random.randrange(40,60,5))
Orc = monster("Orc","A",random.randrange(60,80,5))
#Rang S & SS
Démon = monster("Démon","S",random.randrange(80,100,5))
Vampire = monster("Vampire","SS",random.randrange(100,120,5))
#Rang SSS
Dragon = monster("Dragon","SSS",random.randrange(120,150,5))
Ange_déchu = monster("Ange déchu","SSS",random.randrange(120,150,5))

all_monster = [Cafard,Slime,Loup,Gobelin,Orc,Démon,Vampire,random.choice((Ange_déchu,Dragon))]
