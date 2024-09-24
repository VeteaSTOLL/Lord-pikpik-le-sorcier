import pygame

class joueur(pygame.sprite.Sprite): #sprite = class de base de tous les élément visible du jeus. On peut mettre a jour, mettre img et changer pos
    def __init__(self):
        super().__init__()
        self.velocity = 2
        
        self.image=pygame.image.load("img/rond_noir.png")
        self.image= pygame.transform.scale(self.image, (50,50))
        
        self.rect= self.image.get_rect()
        self.rect.x=400
        self.rect.y= 670
        
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity    
        
