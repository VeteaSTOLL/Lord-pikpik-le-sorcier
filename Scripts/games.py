import pygame
from joueur import joueur
from joueur import roulette
from platformClass import Platform
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
        
        #////////////////PLATEFRORMS//////////
        
        # Liste des rectangles de plateformes
        self.platform_lis_rect = [pygame.Rect(50, 600, 300, 50), pygame.Rect(400, 450, 300, 50)] #(x,y (point supp gauche),largeur,hauteur)

        # Liste des plateformes
        self.platforms = []
        
        # Créer des objets Platform à partir de la liste des rectangles
        for rect in self.platform_lis_rect:
            platform = Platform(rect)
            self.platforms.append(platform)  # Ajouter les plateformes à la liste
        
    def display_platforms(self, surface):
        # Parcourir et afficher chaque plateforme dans la liste
        for platform in self.platforms:
            platform.display(surface)

    def check_collisions(self):
        #Vérifie les collisions du joueur avec les plateformes
        player_rect = self.joueur.rect

        # Parcourir les plateformes
        for platform in self.platforms:
            if player_rect.colliderect(platform.rect):
                # Si le joueur est en train de descendre et touche une plateforme
                if self.joueur.velocity_y > 0 and player_rect.bottom <= platform.rect.top + 10:
                    self.joueur.rect.bottom = platform.rect.top  # Positionner le joueur sur le dessus de la plateforme
                    self.joueur.pos_y = self.joueur.rect.y  # Corriger la position en y
                    self.joueur.velocity_y = 0  # Arrêter la chute
                    self.joueur.is_jumping = False  # Il n'est plus en saut
                    break
        #else:
            # Si aucune collision, le joueur est en l'air
            # self.joueur.is_jumping = True
