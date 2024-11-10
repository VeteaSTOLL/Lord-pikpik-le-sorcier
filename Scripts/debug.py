from collections.abc import Iterable
import pygame

class debug(): 
    def __init__(self):
        pygame.font.init()
        self.debug_mode = False

        self.font = pygame.font.SysFont('arial', 30)
        self.grid_color = (255,0,0)
        self.grid_size = 50
        self.circle_color = (255,0,0)


    def draw(self, screen, body, pos, fps):        
        self.draw_grid(screen, self.grid_color, self.grid_size)
        self.draw_destination(pos, body, screen, self.circle_color)
        self.draw_infos(screen, fps, pos)


    def draw_grid(self, screen, line_color, grid_size):
        for i in range(screen.get_width()//grid_size + 1):
            # colonnes
            pygame.draw.line(screen, line_color, (i*grid_size, 0), (i*grid_size, screen.get_height()))
        
        for i in range(screen.get_height()//grid_size + 1):
            # lignes
            pygame.draw.line(screen, line_color, (0, i*grid_size), (screen.get_width(), i*grid_size))
            
    def draw_destination(self, destination, body, screen, circle_color):
        for i in range(5):
            for j in range(5):
                if body[i][j] != 0:
                    pygame.draw.circle(screen, circle_color, ((destination[0] + j)*50 + 25, (destination[1] + i)*50 + 25), 5)

        pygame.draw.circle(screen, (255-circle_color[0],255-circle_color[1],255-circle_color[2]), (destination[0]*50 + 25, destination[1]*50 + 25), 10)

    def draw_infos(self, screen, fps, pos):
        fps_text = self.font.render('fps : ' + str(round(fps)), False, (0, 0, 0))
        pos_text = self.font.render(f'x : {int(pos[0])}, y : {int(pos[1])}', False, (0, 0, 0))

        screen.blit(fps_text, (10,0))
        screen.blit(pos_text, (10,30))