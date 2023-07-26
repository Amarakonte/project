import item
import map
import game
from pickle import *

class player:   
    def __init__(self,name,type_aventurer):
        self.name = name
        self.location_name = "Forêt"
        self.locationID = 7
        self.type_aventurer = type_aventurer
        self.pos_x = 1
        self.pos_y = 1
        self.level = 1
        self.max_xp = 100
        self.xp = 0
        self.inventory = []
        self.money = 0
        self.profile = {"weapon" : item.nonew, "armor" :item.nonea }
        if type_aventurer == "Warrior":
            self.dodge = 50
            self.force = 200 + 200
            self.defense = 150 + 150
            self.crit = 100
            self.pv_max = 300 + 300
            self.pv = self.pv_max
            self.mana_max = 250
            self.mana = self.mana_max
            self.inventory.append(item.Sword_1)
        elif type_aventurer == "Wizard":
            self.dodge = 50
            self.force = 200 + 200
            self.defense = 150
            self.crit = 100
            self.pv_max = 300
            self.pv = self.pv_max
            self.mana_max = 250 + 250
            self.mana = self.mana_max
            self.inventory.append(item.Staff_1)
        elif type_aventurer == "Archer":
            self.dodge = 50
            self.force = 200 + 200
            self.defense = 150
            self.crit = 100 + 100
            self.pv_max = 300
            self.pv = self.pv_max
            self.mana_max = 250
            self.mana = self.mana_max
            self.inventory.append(item.Bow_1)
        elif type_aventurer == "Ninja":
            self.dodge = 50 + 50
            self.force = 200
            self.defense = 150
            self.crit = 100 + 100
            self.pv_max = 300
            self.pv = self.pv_max
            self.mana_max = 250 + 250
            self.mana = self.mana_max
            self.inventory.append(item.Dagger_1)
            
    
    def profil():
        w = game.Joueur.profile["weapon"]
        a = game.Joueur.profile["armor"]
        print("__PROFIL__\nName :", game.Joueur.name , "\nClass :",game.Joueur.type_aventurer, "\nLevel :" , game.Joueur.level ,"\nXP :",game.Joueur.xp ,"/",game.Joueur.max_xp, "\nPV :"  , game.Joueur.pv,"/",game.Joueur.pv_max,"\nPM :"  , game.Joueur.mana,"/",game.Joueur.mana_max, "\nForce :" , game.Joueur.force , "\nDefense :" , game.Joueur.defense , "\nDodge :" , game.Joueur.dodge, "\nCritical :", game.Joueur.crit)
        print("__EQUIPED__\nWeapon :",w.name,w.level,"\nArmor :",a.name,a.level)
    
    def show_inventory(inventory):
        print("__INVENTORY__")
        i = 0
        if inventory != [] :
            for x in inventory:
                i += 1
                print(i,"-",x.name,"lv:",x.level)
        else :
            print("-- Vide --")
        
        
            
    def add_item(item):
        game.Joueur.inventory.append(item)
                    
    def sell_item(self,numbercase):
        if self.inventory[numbercase] == 0:
            pass
                
    def level_up(self):
        if self.xp >= self.max_xp:
            self.max_xp *= round(1.2)
            self.level += 1
            self.xp = 0
            self.dodge += self.dodge
            self.force += self.force
            self.defense += self.defense
            self.pv_max += self.pv_max
            self.pv = self.pv_max
            self.mana_max += self.mana_max
            self.mana = self.mana_max
            print("-- Vous avez évolué au niveau ",self.level,"--")
            
    def take_weapon():
        take = int(input("Quel objet voulez-vous équipé ?\n"))
        take -= 1
        x = game.Joueur.inventory[take]
        if x.restriction == game.Joueur.type_aventurer :
            if x.type == "armor":
                if game.Joueur.profile["armor"].name == "none":
                    game.Joueur.profile["armor"] = x
                    print("Vous avez équipé :",x.name)
                    del game.Joueur.inventory[take]
                else:
                    player.add_item(game.Joueur.profile["armor"])
                    y = game.Joueur.profile["armor"]
                    print("L'ancien équipement est déséquiper :",y.name)
                    game.Joueur.profile["armor"] = x
                    print("Vous avez équipé :",x.name)
                    del game.Joueur.inventory[take]
            if x.type == "weapon":
                if game.Joueur.profile["weapon"].name == "none":
                    game.Joueur.profile["weapon"] = x
                    print("Vous avez équipé :",x.name)
                    del game.Joueur.inventory[take]
                else:
                    player.add_item(game.Joueur.profile["weapon"])
                    y = game.Joueur.profile["weapon"]
                    print("L'ancien équipement est déséquiper :",y.name)
                    game.Joueur.profile["weapon"] = x
                    print("Vous avez équipé :",x.name)
                    del game.Joueur.inventory[take]
        else :
            print("Vous ne pouvez pas équipé cet objet !")
