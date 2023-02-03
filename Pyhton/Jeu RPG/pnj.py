import game


class pnj:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        if self.type == "Quete":
            self.description = "Je suis un donneur de quête !"
            self.inventory = {"1 - Quête rang D" : ["Vaincre 10 monstres dans une carte rang D"],
                               "2 - Quête rang C" : ["Vaincre 10 monstres dans une carte rang C"],
                               "3 - Quête rang B" : ["Vaincre 10 monstres dans une carte rang B"],
                               "4 - Quête rang A" : ["Vaincre 10 monstres dans une carte rang A"],
                               "5 - Quête rang S" : ["Vaincre 10 monstres dans une carte rang S"],
                               "6 - Quête rang SS" : ["Vaincre 10 monstres dans une carte rang SS"],
                               "7 - Quête rang SSS" : ["Vaincre 10 monstres dans une carte rang SSS"]
                            }
        elif self.type == "Marchand":
            self.description = "Je suis un marchand ambulant!"
            self.inventory = {"1 - Potion de vie : 100$" : 100,
                            "2 - Potion de force : 100$" : 100,
                            "3 - Potion de défense : 100$" : 100,
                            "4 - Potion de d'esquive : 100$" : 100,
                            "5 - Potion de critique : 100$" : 100
                            }
             
    def presentation(self):
        print("Bonjour",game.Joueur.name,"!\nJe me présente je m'appelle",self.name,"le pnj\n",self.description)
        for x in self.inventory:
            print(x)
        
        
        
        

Quete = pnj("Bob","Quete")
Marchand = pnj("Marc","Marchand")




