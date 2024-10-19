import pygame

class collision():
    def __init__(self, x, y, dx, dy):
        self.position = [x,y]
        self.size = [dx,dy]
        self.color = (0,255,0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0] * 50, self.position[1] * 50, self.size[0] * 50, self.size[1] * 50))

class collision_list():
    def __init__(self):        
        self.collisions = []

        self.collisions.append(collision(1,12,6,3))
        self.collisions.append(collision(8,9,6,1))
        self.collisions.append(collision(11,14,1,1))

    def draw_collisions(self, screen):
        for c in self.collisions:
            c.draw(screen)

    def check_collision(self, coords):
        for c in self.collisions:
            if (c.position[0] <= coords[0] and coords[0] < c.position[0]+c.size[0]) and (c.position[1] <= coords[1] and coords[1] < c.position[1]+c.size[1]):
                return True
        return False