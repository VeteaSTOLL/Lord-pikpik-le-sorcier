import pygame
from math import sqrt

class joueur(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        #déplacements
        self.speed = 300

        #saut
        self.t = 0 #le temps qu'on passe en l'air
        self.jump_height = 3
        self.gravity = 1500
        self.b = 2*sqrt(self.jump_height * 50 * self.gravity) #variable correspondant au coefficient b d'un polynome du second degré
        self.is_jumping = False   

        #collisions
        self.lower_collision = False
        self.upper_collision = False


        #sprite
        self.image = pygame.image.load("img/rond_noir.png")
        self.image = pygame.transform.scale(self.image, (50, 50))        
        self.rect = self.image.get_rect()
        
        #coordonnées
        self.rect.x = 400
        self.rect.y = 650

        self.pos = [400.0, 650.0]
        self.destination = [8,13]

    def move(self, direction, collision_list):
        if not collision_list.check_collision((self.destination[0]+direction, self.destination[1])):
            self.destination[0] += direction
    
    def update_pos(self, dt):        
        direction = (self.destination[0]*50 - self.pos[0] > 0) * 2 - 1
        self.pos[0] += self.speed * dt * direction
        self.rect.x = self.pos[0]
    
    def apply_gravity(self, dt, collision_list):
        if not self.lower_collision or self.is_jumping: # si on est en l'air ou qu'on a sauté
            self.t += dt #on augmente le temps passé en l'air
            self.pos[1] += (2 * self.gravity * self.t - self.b) * dt #des maths bizarre (la dérivée de ax² + bx avec a := gravity et b := b)
        self.destination[1] = self.pos[1] // 50 #on update destination

        self.lower_collision = collision_list.check_collision((self.destination[0], self.destination[1]+1)) #on regarde si il y a une collision en dessous de nous

        if self.lower_collision and self.t > self.b / (2*self.gravity):
            #si on touche une collision en décendant:
            self.pos[1] = self.destination[1] * 50 #on case bien le joueur

            self.is_jumping = False
            self.t = 0 # on réinitialise le timer

        self.upper_collision = collision_list.check_collision((self.destination[0], self.destination[1])) #on regarde si il y a une collision en dessus de nous

        if (not self.lower_collision and not self.is_jumping) or self.upper_collision: # si on est en l'air mais qu'on ne saute pas ou qu'il y a une collision au dessus de nous
            self.t = self.b / (2*self.gravity) # on passe directement à la descente sans passer par l'ascension
            self.is_jumping = True # on met is_jumping à true pour ne pas refaire ce qu'il y a dans cette condition
            if self.upper_collision:
                self.pos[1] = (self.destination[1]+1)*50
            
        self.rect.y = self.pos[1] #on update l'affichage    
        

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
        self.rect.y = 650
