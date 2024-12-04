# level_manager.py
from level import Level
from objets import item_manager
from joueur import *

class Level_manager:
    def __init__(self):
        self.item_manager = item_manager()
        self.nb_level = 2
        self.levels=[
            {
                "collisions" : [                
                    (0, 14, 13, 4),
                    (15, 14, 20, 4),
                    (5, 10, 3, 4),
                    (17, 9, 3, 5)
                ]  ,
                
                "items" :[
                    (self.item_manager.porte, 18, 8, 1, 1),
                    (self.item_manager.roulette, 6, 9, 1, 1),
                    (self.item_manager.roulette, 3,13, 1, 1),
                    (self.item_manager.botte, 4, 13, 1, 1),                  
                ]         
            },
            {
                "collisions" :[
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
                ],
                
                "items":[
                    (self.item_manager.roulette, 3, 13, 1, 1)
                ]
            }

        ]


    def creer_niveau(self, current_level):
        level = self.levels[current_level-1]
        collisions_elem = level["collisions"]
        objets_elem = level["items"]
        return Level(collisions_elem, objets_elem)
