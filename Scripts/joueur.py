import pygame
from math import sqrt

class joueur(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        #déplacements
        self.speed = 300
        self.direction = 0
        self.can_move = True
        self.can_jump = False

        #saut
        self.t = 0 #le temps qu'on passe en l'air
        self.jump_height = 3
        self.gravity = 1500
        self.b = 2*sqrt(self.jump_height * 50 * self.gravity) #variable correspondant au coefficient b d'un polynome du second degré calculé pour avoir la hauteur de saut désirée
        self.is_jumping = False   

        #collisions
        self.lower_collision = False
        self.upper_collision = False

        #forme du perso
        self.body = [[0,0,0,0,0],
                     [0,0,0,0,0],
                     [0,0,1,0,0],
                     [0,0,0,0,0],
                     [0,0,0,0,0]]

        #sprite
        self.image = pygame.image.load("img/rond_noir.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        #coordonnées

        self.pos = [0*50,11*50]
        self.destination = [0,11]

    def move(self, direction, collision_list):
        if not collision_list.check_collision_player((self.destination[0]+direction, self.destination[1]), self.body):
            self.destination[0] += direction
            self.direction = direction
        else:            
            self.direction = 0
    
    def check_inputs(self, left, right, collision_list):
        if left:
            self.move(-1, collision_list)
        elif right:
            self.move(1, collision_list)
        else:
            return False
        return True

    def update_movement(self, left, right, dt, collision_list):
        self.pos[0] += self.speed * dt * self.direction
        if self.direction != 0 and self.pos[0] * self.direction >= self.destination[0] * 50 * self.direction:
            if not self.check_inputs(left, right, collision_list):
                self.pos[0] = self.destination[0] * 50
                self.direction = 0
        elif self.direction == 0:
            self.check_inputs(left, right, collision_list)

    
    def apply_gravity(self, dt, collision_list):
        if not self.lower_collision or self.is_jumping: # si on est en l'air ou qu'on a sauté
            self.t += dt #on augmente le temps passé en l'air
            self.pos[1] += (2 * self.gravity * self.t - self.b) * dt #des maths bizarre (la dérivée de ax² + bx avec a := gravity et b := b)
        self.destination[1] = self.pos[1] // 50 #on update destination

        self.lower_collision = collision_list.check_collision_player((self.destination[0], self.destination[1]+1), self.body) #on regarde si il y a une collision en dessous de nous

        if self.lower_collision and self.t > self.b / (2*self.gravity):
            #si on touche une collision en décendant:
            self.pos[1] = self.destination[1] * 50 #on case bien le joueur

            self.is_jumping = False
            self.t = 0 # on réinitialise le timer

        self.upper_collision = collision_list.check_collision_player((self.destination[0], self.destination[1]), self.body) #on regarde si il y a une collision en dessus de nous

        if (not self.lower_collision and not self.is_jumping) or self.upper_collision: # si on est en l'air mais qu'on ne saute pas ou qu'il y a une collision au dessus de nous
            self.t = self.b / (2*self.gravity) # on passe directement à la descente sans passer par l'ascension
            self.is_jumping = True # on met is_jumping à true pour ne pas refaire ce qu'il y a dans cette condition
            if self.upper_collision:
                self.pos[1] = (self.destination[1]+1)*50
            
        self.destination[1] = self.pos[1] // 50 #on update destination pour les autres scripts
        

    def jump(self):
        #Fait sauter le joueur s'il n'est pas déjà en train de sauter.
        if not self.is_jumping:
            self.is_jumping = True
    
    def draw(self, screen, item_types):
        for i in range(5):
            for j in range(5):
                bodypart = self.body[i][j]
                if bodypart == 1:
                    screen.blit(self.image, pygame.Rect(self.pos[0] + 50 * j, self.pos[1] + 50 * i, 50, 50))
                elif bodypart >= 2:
                    screen.blit(item_types[bodypart-2].image, pygame.Rect(self.pos[0] + 50 * j, self.pos[1] + 50 * i, 50, 50))
    
    def check_body(self):
        nb_1 = 0 
        nb_i = 0
        for i in range(5):
            for j in range(5):
                
                if self.body[i][j] == 1:
                    nb_1 += 1
                if self.body[i][j] != 0 and self.body[i][j] != 1:
                    nb_i += 1
                    
                if nb_1 == 1: 
                    self.can_move = True
                elif nb_1 != 1 and nb_i == 0:
                    self.can_move = False
                    
                
                if self.body[i-1][j] == 1:
                    if self.body[i][j] == 3:  
                        self.can_jump = True
                        self.can_move = True
                    if self.body[i][j] == 2: 
                        self.can_move = True 
                    