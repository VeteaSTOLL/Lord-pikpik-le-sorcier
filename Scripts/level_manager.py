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
        
        self.video = "video/End.mp4"
        
        
        self.nb_level = 5
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
                "collisions": [
                    (0, -1, 20, 1),  #Plafond
                    (20, 0, 3, 16),  #bord écran droit
                    (-1, 0, 1, 16),  #Bord écran gauche
                    (0, 14, 23, 4),  #sol
                    (6, 12, 3, 1),  
                    (12, 10, 4, 1),  
                    (3, 8, 3, 1),    
                    (8, 6, 2, 1),    
                    (15, 4, 2, 1),   
                    (2, 4, 2, 1),    
                    (10, 13, 1, 1), 
                    (16, 13, 1, 1), 
                    (5, 9, 1, 1),    
                ],

                "items": [
                    (self.item_manager.porte, 16, 3, 1, 1),    
                    (self.item_manager.botte, 7, 11, 1, 1),     
                    (self.item_manager.roulette, 5, 7, 1, 1),
                ]
            },
            {
                "collisions" :[
                    (0, -1, 20, 1),#Plafond
                    (20, 0, 3, 16), #bord écran droit
                    (-1, 0, 1, 16),#Bord écran gauche
                    (0, 14, 23, 4), #sol
                    (0,1,1,1),
                    (18,12,1,1),
                    (17,11,1,1),
                    (16,10,1,1),
                    (19,9,1,2),
                    (18,8,1,1),
                    (16,8,1,2),
                    (13,8,4,1),
                    (6,8,1,1),
                    (19,5,1,4),
                    (2,4,1,5),
                    (3,8,1,1),
                    (15,2,3,1),
                    (11,4,3,1),
                    (9,3,1,1),
                    (4,4,1,1),
                    (7,2,1,1),
                ],
                
                "items":[
                    (self.item_manager.porte, 0, 0, 1, 1),
                    (self.item_manager.botte, 18, 13, 1, 1),
                    (self.item_manager.roulette, 16, 7, 1, 1)

                ]
            },
            {
                "collisions" :[
                    (0, -1, 20, 1),#Plafond
                    (23, 0, 3, 16), #bord écran droit
                    (-1, 0, 1, 16),#Bord écran gauche
                    (1, 15, 2, 4), #sol
                    (5, 15, 2, 4),
                    (9, 15, 2, 4),
                    (14, 15, 2, 4),
                    (18, 11, 5, 1),
                    (21, 7, 2, 1),
                    (17, 3, 2, 1),
                    (12, 3, 2, 1),
                    (6, 7, 2, 1),
                    (3, 5, 1, 1),   
                ],
                
                "items":[
                    (self.item_manager.botte, 1, 14, 1, 1),
                    (self.item_manager.roulette, 2, 14, 1, 1),
                    (self.item_manager.porte, 3, 4, 1, 1)
                    ],           
            },
            {
                "collisions" :[
                    (20, 0, 3, 16),  #bord écran droit
                    (-1, 0, 1, 16),  #Bord écran gauche
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
    
