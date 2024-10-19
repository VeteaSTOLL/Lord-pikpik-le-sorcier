import pygame
from joueur import joueur
from joueur import roulette
from collisions import collision_list
from debug import *


class Game:
    def __init__(self):
        #generer notre joueur
        self.roulette = roulette()
        self.joueur = joueur()
        self.debug = debug()
        
        self.pressed = {}
        self.pressed_down = {}
        self.pressed_up = {}

        self.crafting_interface = False
        
        self.collision_list = collision_list()    