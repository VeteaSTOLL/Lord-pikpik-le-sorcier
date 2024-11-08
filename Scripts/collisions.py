import pygame

class collision():
    def __init__(self, x, y, dx, dy, c = (50,50,50)):
        self.position = [x,y]
        self.size = [dx,dy]
        self.color = c

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0] * 50, self.position[1] * 50, self.size[0] * 50, self.size[1] * 50))

class collision_list():
    def __init__(self):        
        self.collisions = []

        self.collisions.append(collision(5,10,3,4))
        self.collisions.append(collision(0,14,13,1))
        self.collisions.append(collision(15,14,20,1))
        self.collisions.append(collision(17,9,3,5))

    def draw_collisions(self, screen):
        for c in self.collisions:
            c.draw(screen)

    def check_collision(self, coords):
        for c in self.collisions:
            if (c.position[0] <= coords[0] and coords[0] < c.position[0]+c.size[0]) and (c.position[1] <= coords[1] and coords[1] < c.position[1]+c.size[1]):
                return True
        return False
    
    def check_collision_player(self, coords, body):
        for i in range(5):
            for j in range(5):
                if body[i][j] != 0 and self.check_collision((coords[0] + j, coords[1] + i)):
                    return True                
        return False