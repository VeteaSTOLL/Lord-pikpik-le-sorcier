import pygame
from joueur import joueur
from interface_craft import *
from collisions import collision_list
from objets import item_list
from debug import *


class Game:
    def __init__(self, screen):
        #generer notre joueur
        
        self.joueur = joueur()
        self.debug = debug()
        
        self.pressed = {}
        self.pressed_down = {}
        self.pressed_up = {}

        self.crafting_interface_is_open = False
        
        self.collision_list = collision_list()
        self.item_list = item_list() 
        self.interface_craft = Interface_Craft(screen.get_width(), screen.get_height())    

        self.screen = screen
        
        self.storage_case = stock_item_case(120, 150, 100, 100)