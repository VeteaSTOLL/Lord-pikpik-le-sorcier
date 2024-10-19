import pygame
from math import sqrt

class joueur(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.speed = 300

        self.t = 0 #le temps qu'on passe en l'air
        self.jump_height = 3
        self.gravity = 1500
        self.b = 2*sqrt(self.jump_height * 50 * self.gravity) #variable correspondant au coefficient b d'un polynome du second degré
        self.is_jumping = False        

        self.image = pygame.image.load("img/rond_noir.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 700
        self.pos = [400.0, 700.0]

        self.destination = [8,14]
        
        self.ground_y = 700

    def move(self, direction):        
        self.destination[0] += direction
    
    def update_pos(self, dt):        
        direction = (self.destination[0]*50 - self.pos[0] > 0) * 2 - 1
        self.pos[0] += self.speed * dt * direction
        self.rect.x = self.pos[0]
    
    def apply_gravity(self, dt):
        if self.rect.y < self.ground_y or self.is_jumping:  
            self.t += dt
            self.pos[1] += (2 * self.gravity * self.t - self.b) * dt
            self.rect.y = self.pos[1]

            if self.rect.y >= self.ground_y:
                self.pos[1] = self.ground_y
                self.rect.y = self.pos[1]

                self.is_jumping = False
                self.t = 0

        self.destination[1] = round(self.pos[1] / 50)

    def jump(self):
        #Fait sauter le joueur s'il n'est pas déjà en train de sauter.
        if not self.is_jumping:
            self.is_jumping = True

class roulette(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("img/roulette.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 670
