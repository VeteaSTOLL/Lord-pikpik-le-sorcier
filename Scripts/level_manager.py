# level_manager.py
from level import Level
from objets import *
from joueur import *

class Level_manager:
    def __init__(self):
        #self.item_type
        self.items = {
            "porte": item("porte", 4, "img/porte.jpg", [False, False, False, False]),
            
            "roulette": item("roulette", 2, "img/roulette.png", [True, False, False, False]),
            
            "botte": item("botte", 3, "img/botte.png", [True, False, False, False])
        }
        self.nb_level = 2

    def creer_niveau(self, numero):
        if numero == 1:
            collisions_elem = [
                (0, 14, 13, 4),
                (15, 14, 20, 4),
                (5, 10, 3, 4),
                (17, 9, 3, 5),
            ]
            objets_elem= [
                (self.items["porte"], 18, 8, 1, 1),
                (self.items["roulette"], 6, 9, 1, 1),
                (self.items["roulette"], 3,13, 1, 1),
                (self.items["botte"], 4, 13, 1, 1)
            ]

        elif numero == 2:
            collisions_elem = [
                (0, 14, 20, 4),
                (2, 5, 1, 5),
                (3, 5, 2, 1),
                (3, 7, 1, 1),
                (6, 5, 1, 5),
                (9, 5, 1, 5),
                (10, 6, 1, 1),
                (11, 7, 1, 1),
                (12, 8, 1, 1),
                (13, 5, 1, 5)
            ]
            objets_elem = [
                (self.items["roulette"], 3, 13, 1, 1)
            ]
        else:
            collisions_elem = []
            objets_elem = []

        return Level(collisions_elem, objets_elem)
