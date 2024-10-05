import pygame
from joueur import joueur

class Game:
    def __init__(self):
        #generer notre joueur
        self.joueur = joueur()
        
        self.pressed = {}
        self.pressed_down = {}
        self.pressed_up = {}

        self.crafting_interface = False
