import pygame
from interface_craft import *
from joueur import *
from level_manager import *

class Button:
    def __init__(self,x,y, image_path, evenement=None):
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft=(x,y)
        self.evenement = evenement
        
            
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    
    def check_click(self,pos):
        souris = pygame.mouse.get_pos()
        
        
        return 
    
    def restart_level(current_level):
        joueur.reset_body()
        Interface_Craft.reset_interface()
        Level_manager.creer_niveau(current_level)
        


    