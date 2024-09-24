import pygame

class joueur(pygame.sprite.Sprite): #sprite = class de base de tous les élément visible du jeu. On peut mettre a jour, mettre img et changer pos
    def __init__(self):
        super().__init__()
        self.velocity = 300 #vitesse du joueur en pixels / secondes
        
        self.image=pygame.image.load("img/rond_noir.png")
        self.image= pygame.transform.scale(self.image, (50,50))
        
        self.rect= self.image.get_rect()
        self.rect.x=400
        self.rect.y=670

        self.pos_x = 400.0
        self.pos_y = 670.0
        
    def move_right(self, dt):
        self.pos_x += self.velocity * dt
        self.rect.x = self.pos_x
        
    def move_left(self, dt):
        self.pos_x -= self.velocity * dt
        self.rect.x = self.pos_x
        
