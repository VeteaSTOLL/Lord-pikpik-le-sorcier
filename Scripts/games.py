import pygame
from joueur import joueur
from interface_craft import *
from collisions import collision_list
from objets import item_manager
from debug import *
from level_manager import Level_manager

class Game:
    def __init__(self, screen):
        #generer notre joueur
        
        self.joueur = joueur()
        self.debug = debug()
        
        self.pressed = {}
        self.pressed_down = {}
        self.pressed_up = {}
        
        self.collision_list = collision_list()
        self.item_manager = item_manager() 
        self.interface_craft = Interface_Craft(screen.get_width(), screen.get_height())
                
        self.level_manager = Level_manager()
