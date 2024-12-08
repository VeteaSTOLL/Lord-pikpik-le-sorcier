import pygame
from level import Level
from objets import item_manager
from joueur import *
from interface_craft import *
from level_manager import*

class Level_manager:
    def __init__(self):
        self.item_manager = item_manager()
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")
        self.door_sound = pygame.mixer.Sound("sounds/door.wav")
        self.nb_level = 3
        self.levels=[
            {
                "collisions" : [                
                    (0, 14, 13, 4),#Sol
                    (20, 0, 1, 16), #bord écran droit
                    (-1, 0, 1, 16),#Bord écran gauche
                    (0, -1, 20, 1),#Plafond
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
                    (0, -1, 20, 1),#Plafond
                    (20, 0, 1, 16), #bord écran droit
                    (-1, 0, 1, 16),#Bord écran gauche
                    (0, 14, 20, 4),
                    (18, 4, 2, 1),
                    (18, 6, 2, 1),
                    (13, 5, 1, 5),
                    (3, 7, 1, 1),
                    (10, 6, 1, 1),
                    (6, 3, 1, 5),
                    (9, 12, 1, 1),

                    
                    
                ],
                
                "items":[
                    (self.item_manager.aile, 3, 13, 1, 1),
                    (self.item_manager.porte, 19,5,1,1),
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
                ]
            }

        ]


    def creer_niveau(self, current_level):
        level = self.levels[current_level-1]
        collisions_elem = level["collisions"]
        objets_elem = level["items"]
        return Level(collisions_elem, objets_elem)
    
    def load_level(self, current_level):
        self.creer_niveau(current_level)
        joueur.reset_body()
        Interface_Craft.reset_interface()
        
        
