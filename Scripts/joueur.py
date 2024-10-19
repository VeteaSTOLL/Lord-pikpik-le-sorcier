import pygame


class joueur(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.velocity = 300  
        self.velocity_y = 0 
        
        self.jump_strength = 1000 
        self.gravity = 3000  
        self.is_jumping = False
        

        self.image = pygame.image.load("img/rond_noir.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 700
        self.pos = [400.0, 700.0]

        self.destination = [8,14]
        
        self.ground_y = 700

    def move_right(self):
        if abs(self.pos[0] - self.destination[0]*50) < 2:
            self.destination[0] += 1
        
    def move_left(self):
        if abs(self.pos[0] - self.destination[0]*50) < 2:
            self.destination[0] -= 1

    def move(self, dt):
        direction = (self.destination[0]*50 - self.pos[0] > 0) * 2 - 1

        self.pos[0] += self.velocity * dt * direction
        self.rect.x = self.pos[0]
    
    def apply_gravity(self, dt):
        #Applique la gravité si le joueur est en l'air.
        if self.rect.y < self.ground_y or self.is_jumping:
            self.velocity_y += self.gravity * dt  # Augmenter la vitesse vers le bas
            self.pos[1] += self.velocity_y * dt  # Mise à jour de la position verticale
            self.rect.y = self.pos[1]
        
            # Si le joueur touche le sol, on arrête le saut et on remet la position y à celle du sol
            if self.rect.y >= self.ground_y:
                self.rect.y = self.ground_y
                self.is_jumping = False
                self.velocity_y = 0  # Le joueur ne tombe plus

    def jump(self):
        #Fait sauter le joueur s'il n'est pas déjà en train de sauter.
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_strength  # Impulsion vers le haut

class roulette(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("img/roulette.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 670
