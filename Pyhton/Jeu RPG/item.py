import game
from random import randint
import character

class potion:
    def __init__(self,name,price,effet,durability):
        self.name = name
        self.price = price
        self.effet = effet
        self.durability = durability

    def use(self):
        x = game.Joueur.inventory
        if self.durability > 1:
            self.durability -= 1
            print("Vous utilisez :", self.name,"\n-- Nombre d'utilisation :",self.durability)
        if self.durability > 0:
            self.durability -= 1
            x.remove(self.name)
            print("Vous utilisez :", self.name,"\n-- Nombre d'utilisation :",self.durability)

class weapon:
    def __init__(self,name,ID,level,attack,defense,dodge,crit,restriction,price,type):
        self.name = name
        self.ID = ID
        self.level = level
        self.attack = attack
        self.defense = defense
        self.dodge = dodge
        self.crit = crit
        self.restriction = restriction
        self.price = price
        self.durability = 100
        self.type = type
      
            
    def use(self):
        x = game.Joueur.profile
        if self.durability > 0:
            self.durability -= 1
        if self.durability == 0:
            print("Votre équipement s'est brisé :",self.name)
            if x["armor"] == self.name :
                x["armor"] = nonea
            if x["weapon"] == self.name :
                x["weapon"] = nonew
    
    def pop_weapon():
        a = [Staff_1,Sword_1,Bow_1,Dagger_1,Staff_5,Sword_5,Bow_5,Dagger_5,Staff_10,Sword_10,Bow_10,Dagger_10,Staff_15,Sword_15,Bow_15,Dagger_15,Staff_20,Sword_20,Bow_20,Dagger_20,Staff_25,Sword_25,Bow_25,Dagger_25,Staff_30,Sword_30,Bow_30,Dagger_30,Staff_35,Sword_35,Bow_35,Dagger_35,Staff_40,Sword_40,Bow_40,Dagger_40,Staff_45,Sword_45,Bow_45,Dagger_45,Staff_50,Sword_50,Bow_50,Dagger_50,Staff_55,Sword_55,Bow_55,Dagger_55,Staff_60,Sword_60,Bow_60,Dagger_60,Staff_65,Sword_65,Bow_65,Dagger_65,Staff_70,Sword_70,Bow_70,Dagger_70,Staff_75,Sword_75,Bow_75,Dagger_75,Staff_80,Sword_80,Bow_80,Dagger_80,Staff_85,Sword_85,Bow_85,Dagger_85,Staff_90,Sword_90,Bow_90,Dagger_90,Staff_95,Sword_95,Bow_95,Dagger_95,Staff_100,Sword_100,Bow_100,Dagger_100,Staff_105,Sword_105,Bow_105,Dagger_105,Staff_110,Sword_110,Bow_110,Dagger_110,Staff_115,Sword_115,Bow_115,Dagger_115,Staff_120,Sword_120,Bow_120,Dagger_120,Staff_125,Sword_125,Bow_125,Dagger_125,Staff_130,Sword_130,Bow_130,Dagger_130,Staff_135,Sword_135,Bow_135,Dagger_135,Staff_140,Sword_140,Bow_140,Dagger_140,Staff_145,Sword_145,Bow_145,Dagger_145,Staff_150,Sword_150,Bow_150,Dagger_150,Armor_1,Mask_1,Cape_1,Dress_1,Armor_5,Mask_5,Cape_5,Dress_5,Armor_10,Mask_10,Cape_10,Dress_10,Armor_15,Mask_15,Cape_15,Dress_15,Armor_20,Mask_20,Cape_20,Dress_20,Armor_25,Mask_25,Cape_25,Dress_25,Armor_30,Mask_30,Cape_30,Dress_30,Armor_35,Mask_35,Cape_35,Dress_35,Armor_40,Mask_40,Cape_40,Dress_40,Armor_45,Mask_45,Cape_45,Dress_45,Armor_50,Mask_50,Cape_50,Dress_50,Armor_55,Mask_55,Cape_55,Dress_55,Armor_60,Mask_60,Cape_60,Dress_60,Armor_65,Mask_65,Cape_65,Dress_65,Armor_70,Mask_70,Cape_70,Dress_70,Armor_75,Mask_75,Cape_75,Dress_75,Armor_80,Mask_80,Cape_80,Dress_80,Armor_85,Mask_85,Cape_85,Dress_85,Armor_90,Mask_90,Cape_90,Dress_90,Armor_95,Mask_95,Cape_95,Dress_95,Armor_100,Mask_100,Cape_100,Dress_100,Armor_105,Mask_105,Cape_105,Dress_105,Armor_110,Mask_110,Cape_110,Dress_110,Armor_115,Mask_115,Cape_115,Dress_115,Armor_120,Mask_120,Cape_120,Dress_120,Armor_125,Mask_125,Cape_125,Dress_125,Armor_130,Mask_130,Cape_130,Dress_130,Armor_135,Mask_135,Cape_135,Dress_135,Armor_140,Mask_140,Cape_140,Dress_140,Armor_145,Mask_145,Cape_145,Dress_145,Armor_150,Mask_150,Cape_150,Dress_150]
        x = a[randint(0,len(a)-1)]
        print("Vous trouvez sur votre passage :",x.name,"!")
        character.player.add_item(x)

#ARME
nonew = weapon("none","none","",0,0,0,0,"",0,"weapon")  
nonea = weapon("none","none","",0,0,0,0,"",0,"armor")      
Staff_1 = weapon("Staff","ST1",1,225,0,0,100,"Wizard",10,"weapon")
Sword_1 = weapon("Sword","SW1",1,225,0,0,100,"Warrior",10,"weapon")
Bow_1 = weapon("Bow","BO1",1,225,0,0,100,"Archer",10,"weapon")
Dagger_1 = weapon("Dagger","DA1",1,225,0,0,100,"Ninja",10,"weapon")

Staff_5 = weapon("Staff","ST5",1,100,0,0,100,"Wizard",10,"weapon")
Sword_5 = weapon("Sword","SW5",1,100,0,0,100,"Warrior",10,"weapon")
Bow_5 = weapon("Bow","BO5",1,100,0,0,100,"Archer",10,"weapon")
Dagger_5 = weapon("Dagger","DA5",1,100,0,0,100,"Ninja",10,"weapon")

Staff_10 = weapon("Staff","ST10",1,100,0,0,100,"Wizard",10,"weapon")
Sword_10 = weapon("Sword","SW10",1,100,0,0,100,"Warrior",10,"weapon")
Bow_10 = weapon("Bow","BO10",1,100,0,0,100,"Archer",10,"weapon")
Dagger_10 = weapon("Dagger","DA10",1,100,0,0,100,"Ninja",10,"weapon")

Staff_15 = weapon("Staff","ST15",1,100,0,0,100,"Wizard",10,"weapon")
Sword_15 = weapon("Sword","SW15",1,100,0,0,100,"Warrior",10,"weapon")
Bow_15 = weapon("Bow","BO15",1,100,0,0,100,"Archer",10,"weapon")
Dagger_15 = weapon("Dagger","DA15",1,100,0,0,100,"Ninja",10,"weapon")

Staff_20 = weapon("Staff","ST20",1,100,0,0,100,"Wizard",10,"weapon")
Sword_20 = weapon("Sword","SW20",1,100,0,0,100,"Warrior",10,"weapon")
Bow_20 = weapon("Bow","BO20",1,100,0,0,100,"Archer",10,"weapon")
Dagger_20 = weapon("Dagger","DA20",1,100,0,0,100,"Ninja",10,"weapon")

Staff_25 = weapon("Staff","ST25",1,100,0,0,100,"Wizard",10,"weapon")
Sword_25 = weapon("Sword","SW25",1,100,0,0,100,"Warrior",10,"weapon")
Bow_25 = weapon("Bow","BO25",1,100,0,0,100,"Archer",10,"weapon")
Dagger_25 = weapon("Dagger","DA25",1,100,0,0,100,"Ninja",10,"weapon")

Staff_30 = weapon("Staff","ST30",1,100,0,0,100,"Wizard",10,"weapon")
Sword_30 = weapon("Sword","SW30",1,100,0,0,100,"Warrior",10,"weapon")
Bow_30 = weapon("Bow","BO30",1,100,0,0,100,"Archer",10,"weapon")
Dagger_30 = weapon("Dagger","DA30",1,100,0,0,100,"Ninja",10,"weapon")

Staff_35 = weapon("Staff","ST35",1,100,0,0,100,"Wizard",10,"weapon")
Sword_35 = weapon("Sword","SW35",1,100,0,0,100,"Warrior",10,"weapon")
Bow_35 = weapon("Bow","BO35",1,100,0,0,100,"Archer",10,"weapon")
Dagger_35 = weapon("Dagger","DA35",1,100,0,0,100,"Ninja",10,"weapon")

Staff_40 = weapon("Staff","ST40",1,100,0,0,100,"Wizard",10,"weapon")
Sword_40 = weapon("Sword","SW40",1,100,0,0,100,"Warrior",10,"weapon")
Bow_40 = weapon("Bow","BO40",1,100,0,0,100,"Archer",10,"weapon")
Dagger_40 = weapon("Dagger","DA40",1,100,0,0,100,"Ninja",10,"weapon")

Staff_45 = weapon("Staff","ST45",1,100,0,0,100,"Wizard",10,"weapon")
Sword_45 = weapon("Sword","SW45",1,100,0,0,100,"Warrior",10,"weapon")
Bow_45 = weapon("Bow","BO45",1,100,0,0,100,"Archer",10,"weapon")
Dagger_45 = weapon("Dagger","DA45",1,100,0,0,100,"Ninja",10,"weapon")

Staff_50 = weapon("Staff","ST50",1,100,0,0,100,"Wizard",10,"weapon")
Sword_50 = weapon("Sword","SW50",1,100,0,0,100,"Warrior",10,"weapon")
Bow_50 = weapon("Bow","BO50",1,100,0,0,100,"Archer",10,"weapon")
Dagger_50 = weapon("Dagger","DA50",1,100,0,0,100,"Ninja",10,"weapon")

Staff_55 = weapon("Staff","ST55",1,100,0,0,100,"Wizard",10,"weapon")
Sword_55 = weapon("Sword","SW55",1,100,0,0,100,"Warrior",10,"weapon")
Bow_55 = weapon("Bow","BO55",1,100,0,0,100,"Archer",10,"weapon")
Dagger_55 = weapon("Dagger","DA55",1,100,0,0,100,"Ninja",10,"weapon")

Staff_60 = weapon("Staff","ST60",1,100,0,0,100,"Wizard",10,"weapon")
Sword_60 = weapon("Sword","SW60",1,100,0,0,100,"Warrior",10,"weapon")
Bow_60 = weapon("Bow","BO60",1,100,0,0,100,"Archer",10,"weapon")
Dagger_60 = weapon("Dagger","DA60",1,100,0,0,100,"Ninja",10,"weapon")

Staff_65 = weapon("Staff","ST65",1,100,0,0,100,"Wizard",10,"weapon")
Sword_65 = weapon("Sword","SW65",1,100,0,0,100,"Warrior",10,"weapon")
Bow_65 = weapon("Bow","BO65",1,100,0,0,100,"Archer",10,"weapon")
Dagger_65 = weapon("Dagger","DA65",1,100,0,0,100,"Ninja",10,"weapon")

Staff_70 = weapon("Staff","ST70",1,100,0,0,100,"Wizard",10,"weapon")
Sword_70 = weapon("Sword","SW70",1,100,0,0,100,"Warrior",10,"weapon")
Bow_70 = weapon("Bow","BO70",1,100,0,0,100,"Archer",10,"weapon")
Dagger_70 = weapon("Dagger","DA70",1,100,0,0,100,"Ninja",10,"weapon")

Staff_75 = weapon("Staff","ST75",1,100,0,0,100,"Wizard",10,"weapon")
Sword_75 = weapon("Sword","SW75",1,100,0,0,100,"Warrior",10,"weapon")
Bow_75 = weapon("Bow","BO75",1,100,0,0,100,"Archer",10,"weapon")
Dagger_75 = weapon("Dagger","DA75",1,100,0,0,100,"Ninja",10,"weapon")

Staff_80 = weapon("Staff","ST80",1,100,0,0,100,"Wizard",10,"weapon")
Sword_80 = weapon("Sword","SW80",1,100,0,0,100,"Warrior",10,"weapon")
Bow_80 = weapon("Bow","BO80",1,100,0,0,100,"Archer",10,"weapon")
Dagger_80 = weapon("Dagger","DA80",1,100,0,0,100,"Ninja",10,"weapon")

Staff_85 = weapon("Staff","ST85",1,100,0,0,100,"Wizard",10,"weapon")
Sword_85 = weapon("Sword","SW85",1,100,0,0,100,"Warrior",10,"weapon")
Bow_85 = weapon("Bow","BO85",1,100,0,0,100,"Archer",10,"weapon")
Dagger_85 = weapon("Dagger","DA85",1,100,0,0,100,"Ninja",10,"weapon")

Staff_90 = weapon("Staff","ST90",1,100,0,0,100,"Wizard",10,"weapon")
Sword_90 = weapon("Sword","SW90",1,100,0,0,100,"Warrior",10,"weapon")
Bow_90 = weapon("Bow","BO90",1,100,0,0,100,"Archer",10,"weapon")
Dagger_90 = weapon("Dagger","DA90",1,100,0,0,100,"Ninja",10,"weapon")

Staff_95 = weapon("Staff","ST95",1,100,0,0,100,"Wizard",10,"weapon")
Sword_95 = weapon("Sword","SW95",1,100,0,0,100,"Warrior",10,"weapon")
Bow_95 = weapon("Bow","BO95",1,100,0,0,100,"Archer",10,"weapon")
Dagger_95 = weapon("Dagger","DA95",1,100,0,0,100,"Ninja",10,"weapon")

Staff_100 = weapon("Staff","ST100",1,100,0,0,100,"Wizard",10,"weapon")
Sword_100 = weapon("Sword","SW100",1,100,0,0,100,"Warrior",10,"weapon")
Bow_100 = weapon("Bow","BO100",1,100,0,0,100,"Archer",10,"weapon")
Dagger_100 = weapon("Dagger","DA100",1,100,0,0,100,"Ninja",10,"weapon")

Staff_105 = weapon("Staff","ST105",1,100,0,0,100,"Wizard",10,"weapon")
Sword_105 = weapon("Sword","SW105",1,100,0,0,100,"Warrior",10,"weapon")
Bow_105 = weapon("Bow","BO105",1,100,0,0,100,"Archer",10,"weapon")
Dagger_105 = weapon("Dagger","DA105",1,100,0,0,100,"Ninja",10,"weapon")

Staff_110 = weapon("Staff","ST110",1,100,0,0,100,"Wizard",10,"weapon")
Sword_110 = weapon("Sword","SW110",1,100,0,0,100,"Warrior",10,"weapon")
Bow_110 = weapon("Bow","BO110",1,100,0,0,100,"Archer",10,"weapon")
Dagger_110 = weapon("Dagger","DA110",1,100,0,0,100,"Ninja",10,"weapon")

Staff_115 = weapon("Staff","ST115",1,100,0,0,100,"Wizard",10,"weapon")
Sword_115 = weapon("Sword","SW115",1,100,0,0,100,"Warrior",10,"weapon")
Bow_115 = weapon("Bow","BO115",1,100,0,0,100,"Archer",10,"weapon")
Dagger_115 = weapon("Dagger","DA115",1,100,0,0,100,"Ninja",10,"weapon")

Staff_120 = weapon("Staff","ST120",1,100,0,0,100,"Wizard",10,"weapon")
Sword_120 = weapon("Sword","SW120",1,100,0,0,100,"Warrior",10,"weapon")
Bow_120 = weapon("Bow","BO120",1,100,0,0,100,"Archer",10,"weapon")
Dagger_120 = weapon("Dagger","DA120",1,100,0,0,100,"Ninja",10,"weapon")

Staff_125 = weapon("Staff","ST125",1,100,0,0,100,"Wizard",10,"weapon")
Sword_125 = weapon("Sword","SW125",1,100,0,0,100,"Warrior",10,"weapon")
Bow_125 = weapon("Bow","BO125",1,100,0,0,100,"Archer",10,"weapon")
Dagger_125 = weapon("Dagger","DA125",1,100,0,0,100,"Ninja",10,"weapon")

Staff_130 = weapon("Staff","ST130",1,100,0,0,100,"Wizard",10,"weapon")
Sword_130 = weapon("Sword","SW130",1,100,0,0,100,"Warrior",10,"weapon")
Bow_130 = weapon("Bow","BO130",1,100,0,0,100,"Archer",10,"weapon")
Dagger_130 = weapon("Dagger","DA130",1,100,0,0,100,"Ninja",10,"weapon")

Staff_135 = weapon("Staff","ST135",1,100,0,0,100,"Wizard",10,"weapon")
Sword_135 = weapon("Sword","SW135",1,100,0,0,100,"Warrior",10,"weapon")
Bow_135 = weapon("Bow","BO135",1,100,0,0,100,"Archer",10,"weapon")
Dagger_135 = weapon("Dagger","DA135",1,100,0,0,100,"Ninja",10,"weapon")

Staff_140 = weapon("Staff","ST140",1,100,0,0,100,"Wizard",10,"weapon")
Sword_140 = weapon("Sword","SW140",1,100,0,0,100,"Warrior",10,"weapon")
Bow_140 = weapon("Bow","BO140",1,100,0,0,100,"Archer",10,"weapon")
Dagger_140 = weapon("Dagger","DA140",1,100,0,0,100,"Ninja",10,"weapon")

Staff_145 = weapon("Staff","ST145",1,100,0,0,100,"Wizard",10,"weapon")
Sword_145 = weapon("Sword","SW145",1,100,0,0,100,"Warrior",10,"weapon")
Bow_145 = weapon("Bow","BO145",1,100,0,0,100,"Archer",10,"weapon")
Dagger_145 = weapon("Dagger","DA145",1,100,0,0,100,"Ninja",10,"weapon")

Staff_150 = weapon("Staff","ST150",1,100,0,0,100,"Wizard",10,"weapon")
Sword_150 = weapon("Sword","SW150",1,100,0,0,100,"Warrior",10,"weapon")
Bow_150 = weapon("Bow","BO150",1,100,0,0,100,"Archer",10,"weapon")
Dagger_150 = weapon("Dagger","DA150",1,100,0,0,100,"Ninja",10,"weapon")

#ARMURE
Armor_1 = weapon("Armor","AR1",1,100,0,50,0,"Warrior",10,"armor")
Mask_1 = weapon("Mask","MA1",1,100,0,50,0,"Ninja",10,"armor")
Cape_1 = weapon("Cape","CA1",1,100,0,50,0,"Wizard",10,"armor")
Dress_1 = weapon("Dress","DR1",1,100,0,50,0,"Archer",10,"armor")

Armor_5 = weapon("Armor","AR5",1,100,0,50,0,"Warrior",10,"armor")
Mask_5 = weapon("Mask","MA5",1,100,0,50,0,"Ninja",10,"armor")
Cape_5 = weapon("Cape","CA5",1,100,0,50,0,"Wizard",10,"armor")
Dress_5 = weapon("Dress","DR5",1,100,0,50,0,"Archer",10,"armor")

Armor_10 = weapon("Armor","AR10",1,100,0,50,0,"Warrior",10,"armor")
Mask_10 = weapon("Mask","MA10",1,100,0,50,0,"Ninja",10,"armor")
Cape_10 = weapon("Cape","CA10",1,100,0,50,0,"Wizard",10,"armor")
Dress_10 = weapon("Dress","DR10",1,100,0,50,0,"Archer",10,"armor")

Armor_15 = weapon("Armor","AR15",1,100,0,50,0,"Warrior",10,"armor")
Mask_15 = weapon("Mask","MA15",1,100,0,50,0,"Ninja",10,"armor")
Cape_15 = weapon("Cape","CA15",1,100,0,50,0,"Wizard",10,"armor")
Dress_15 = weapon("Dress","DR15",1,100,0,50,0,"Archer",10,"armor")

Armor_20 = weapon("Armor","AR20",1,100,0,50,0,"Warrior",10,"armor")
Mask_20 = weapon("Mask","MA20",1,100,0,50,0,"Ninja",10,"armor")
Cape_20 = weapon("Cape","CA20",1,100,0,50,0,"Wizard",10,"armor")
Dress_20 = weapon("Dress","DR20",1,100,0,50,0,"Archer",10,"armor")

Armor_25 = weapon("Armor","AR25",1,100,0,50,0,"Warrior",10,"armor")
Mask_25 = weapon("Mask","MA25",1,100,0,50,0,"Ninja",10,"armor")
Cape_25 = weapon("Cape","CA25",1,100,0,50,0,"Wizard",10,"armor")
Dress_25 = weapon("Dress","DR25",1,100,0,50,0,"Archer",10,"armor")

Armor_30 = weapon("Armor","AR30",1,100,0,50,0,"Warrior",10,"armor")
Mask_30 = weapon("Mask","MA30",1,100,0,50,0,"Ninja",10,"armor")
Cape_30 = weapon("Cape","CA30",1,100,0,50,0,"Wizard",10,"armor")
Dress_30 = weapon("Dress","DR30",1,100,0,50,0,"Archer",10,"armor")

Armor_35 = weapon("Armor","AR35",1,100,0,50,0,"Warrior",10,"armor")
Mask_35 = weapon("Mask","MA35",1,100,0,50,0,"Ninja",10,"armor")
Cape_35 = weapon("Cape","CA35",1,100,0,50,0,"Wizard",10,"armor")
Dress_35 = weapon("Dress","DR35",1,100,0,50,0,"Archer",10,"armor")

Armor_40 = weapon("Armor","AR40",1,100,0,50,0,"Warrior",10,"armor")
Mask_40 = weapon("Mask","MA40",1,100,0,50,0,"Ninja",10,"armor")
Cape_40 = weapon("Cape","CA40",1,100,0,50,0,"Wizard",10,"armor")
Dress_40 = weapon("Dress","DR40",1,100,0,50,0,"Archer",10,"armor")

Armor_45 = weapon("Armor","AR45",1,100,0,50,0,"Warrior",10,"armor")
Mask_45 = weapon("Mask","MA45",1,100,0,50,0,"Ninja",10,"armor")
Cape_45 = weapon("Cape","CA45",1,100,0,50,0,"Wizard",10,"armor")
Dress_45 = weapon("Dress","DR45",1,100,0,50,0,"Archer",10,"armor")

Armor_50 = weapon("Armor","AR50",1,100,0,50,0,"Warrior",10,"armor")
Mask_50 = weapon("Mask","MA50",1,100,0,50,0,"Ninja",10,"armor")
Cape_50 = weapon("Cape","CA50",1,100,0,50,0,"Wizard",10,"armor")
Dress_50 = weapon("Dress","DR50",1,100,0,50,0,"Archer",10,"armor")

Armor_55 = weapon("Armor","AR55",1,100,0,50,0,"Warrior",10,"armor")
Mask_55 = weapon("Mask","MA55",1,100,0,50,0,"Ninja",10,"armor")
Cape_55 = weapon("Cape","CA55",1,100,0,50,0,"Wizard",10,"armor")
Dress_55 = weapon("Dress","DR55",1,100,0,50,0,"Archer",10,"armor")

Armor_60 = weapon("Armor","AR60",1,100,0,50,0,"Warrior",10,"armor")
Mask_60 = weapon("Mask","MA60",1,100,0,50,0,"Ninja",10,"armor")
Cape_60 = weapon("Cape","CA60",1,100,0,50,0,"Wizard",10,"armor")
Dress_60 = weapon("Dress","DR60",1,100,0,50,0,"Archer",10,"armor")

Armor_65 = weapon("Armor","AR65",1,100,0,50,0,"Warrior",10,"armor")
Mask_65 = weapon("Mask","MA65",1,100,0,50,0,"Ninja",10,"armor")
Cape_65 = weapon("Cape","CA65",1,100,0,50,0,"Wizard",10,"armor")
Dress_65 = weapon("Dress","DR65",1,100,0,50,0,"Archer",10,"armor")

Armor_70 = weapon("Armor","AR70",1,100,0,50,0,"Warrior",10,"armor")
Mask_70 = weapon("Mask","MA70",1,100,0,50,0,"Ninja",10,"armor")
Cape_70 = weapon("Cape","CA70",1,100,0,50,0,"Wizard",10,"armor")
Dress_70 = weapon("Dress","DR70",1,100,0,50,0,"Archer",10,"armor")

Armor_75 = weapon("Armor","AR75",1,100,0,50,0,"Warrior",10,"armor")
Mask_75 = weapon("Mask","MA75",1,100,0,50,0,"Ninja",10,"armor")
Cape_75 = weapon("Cape","CA75",1,100,0,50,0,"Wizard",10,"armor")
Dress_75 = weapon("Dress","DR75",1,100,0,50,0,"Archer",10,"armor")

Armor_80 = weapon("Armor","AR80",1,100,0,50,0,"Warrior",10,"armor")
Mask_80 = weapon("Mask","MA80",1,100,0,50,0,"Ninja",10,"armor")
Cape_80 = weapon("Cape","CA80",1,100,0,50,0,"Wizard",10,"armor")
Dress_80 = weapon("Dress","DR80",1,100,0,50,0,"Archer",10,"armor")

Armor_85 = weapon("Armor","AR85",1,100,0,50,0,"Warrior",10,"armor")
Mask_85 = weapon("Mask","MA85",1,100,0,50,0,"Ninja",10,"armor")
Cape_85 = weapon("Cape","CA85",1,100,0,50,0,"Wizard",10,"armor")
Dress_85 = weapon("Dress","DR85",1,100,0,50,0,"Archer",10,"armor")

Armor_90 = weapon("Armor","AR90",1,100,0,50,0,"Warrior",10,"armor")
Mask_90 = weapon("Mask","MA90",1,100,0,50,0,"Ninja",10,"armor")
Cape_90 = weapon("Cape","CA90",1,100,0,50,0,"Wizard",10,"armor")
Dress_90 = weapon("Dress","DR90",1,100,0,50,0,"Archer",10,"armor")

Armor_95 = weapon("Armor","AR95",1,100,0,50,0,"Warrior",10,"armor")
Mask_95 = weapon("Mask","MA95",1,100,0,50,0,"Ninja",10,"armor")
Cape_95 = weapon("Cape","CA95",1,100,0,50,0,"Wizard",10,"armor")
Dress_95 = weapon("Dress","DR95",1,100,0,50,0,"Archer",10,"armor")

Armor_100 = weapon("Armor","AR100",1,100,0,50,0,"Warrior",10,"armor")
Mask_100 = weapon("Mask","MA100",1,100,0,50,0,"Ninja",10,"armor")
Cape_100 = weapon("Cape","CA100",1,100,0,50,0,"Wizard",10,"armor")
Dress_100 = weapon("Dress","DR100",1,100,0,50,0,"Archer",10,"armor")

Armor_105 = weapon("Armor","AR105",1,100,0,50,0,"Warrior",10,"armor")
Mask_105 = weapon("Mask","MA105",1,100,0,50,0,"Ninja",10,"armor")
Cape_105 = weapon("Cape","CA105",1,100,0,50,0,"Wizard",10,"armor")
Dress_105 = weapon("Dress","DR105",1,100,0,50,0,"Archer",10,"armor")

Armor_110 = weapon("Armor","AR110",1,100,0,50,0,"Warrior",10,"armor")
Mask_110 = weapon("Mask","MA110",1,100,0,50,0,"Ninja",10,"armor")
Cape_110 = weapon("Cape","CA110",1,100,0,50,0,"Wizard",10,"armor")
Dress_110 = weapon("Dress","DR110",1,100,0,50,0,"Archer",10,"armor")

Armor_115 = weapon("Armor","AR115",1,100,0,50,0,"Warrior",10,"armor")
Mask_115 = weapon("Mask","MA115",1,100,0,50,0,"Ninja",10,"armor")
Cape_115 = weapon("Cape","CA115",1,100,0,50,0,"Wizard",10,"armor")
Dress_115 = weapon("Dress","DR115",1,100,0,50,0,"Archer",10,"armor")

Armor_120 = weapon("Armor","AR120",1,100,0,50,0,"Warrior",10,"armor")
Mask_120 = weapon("Mask","MA120",1,100,0,50,0,"Ninja",10,"armor")
Cape_120 = weapon("Cape","CA120",1,100,0,50,0,"Wizard",10,"armor")
Dress_120 = weapon("Dress","DR120",1,100,0,50,0,"Archer",10,"armor")

Armor_125 = weapon("Armor","AR125",1,100,0,50,0,"Warrior",10,"armor")
Mask_125 = weapon("Mask","MA125",1,100,0,50,0,"Ninja",10,"armor")
Cape_125 = weapon("Cape","CA125",1,100,0,50,0,"Wizard",10,"armor")
Dress_125 = weapon("Dress","DR125",1,100,0,50,0,"Archer",10,"armor")

Armor_130 = weapon("Armor","AR130",1,100,0,50,0,"Warrior",10,"armor")
Mask_130 = weapon("Mask","MA130",1,100,0,50,0,"Ninja",10,"armor")
Cape_130 = weapon("Cape","CA130",1,100,0,50,0,"Wizard",10,"armor")
Dress_130 = weapon("Dress","DR130",1,100,0,50,0,"Archer",10,"armor")

Armor_135 = weapon("Armor","AR135",1,100,0,50,0,"Warrior",10,"armor")
Mask_135 = weapon("Mask","MA135",1,100,0,50,0,"Ninja",10,"armor")
Cape_135 = weapon("Cape","CA135",1,100,0,50,0,"Wizard",10,"armor")
Dress_135 = weapon("Dress","DR135",1,100,0,50,0,"Archer",10,"armor")

Armor_140 = weapon("Armor","AR140",1,100,0,50,0,"Warrior",10,"armor")
Mask_140 = weapon("Mask","MA140",1,100,0,50,0,"Ninja",10,"armor")
Cape_140 = weapon("Cape","CA140",1,100,0,50,0,"Wizard",10,"armor")
Dress_140 = weapon("Dress","DR140",1,100,0,50,0,"Archer",10,"armor")

Armor_145 = weapon("Armor","AR145",1,100,0,50,0,"Warrior",10,"armor")
Mask_145 = weapon("Mask","MA145",1,100,0,50,0,"Ninja",10,"armor")
Cape_145 = weapon("Cape","CA145",1,100,0,50,0,"Wizard",10,"armor")
Dress_145 = weapon("Dress","DR145",1,100,0,50,0,"Archer",10,"armor")

Armor_150 = weapon("Armor","AR150",1,100,0,50,0,"Warrior",10,"armor")
Mask_150 = weapon("Mask","MA150",1,100,0,50,0,"Ninja",10,"armor")
Cape_150 = weapon("Cape","CA150",1,100,0,50,0,"Wizard",10,"armor")
Dress_150 = weapon("Dress","DR150",1,100,0,50,0,"Archer",10,"armor")