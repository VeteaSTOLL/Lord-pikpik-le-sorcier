import pygame
from joueur import joueur

class Game:
    def __init__(self):
        #generer notre joueur
        self.joueur = joueur()
        self.pressed ={}
