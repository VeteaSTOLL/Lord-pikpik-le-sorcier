import pygame

class debug(): 
    def __init__(self):
        self.debug_mode = False

    def draw_grid(self, screen, line_color, grid_size):
        if self.debug_mode:
            for i in range(screen.get_width()//grid_size + 1):
                # colonnes
                pygame.draw.line(screen, line_color, (i*grid_size, 0), (i*grid_size, screen.get_height()))
            
            for i in range(screen.get_height()//grid_size + 1):
                # lignes
                pygame.draw.line(screen, line_color, (0, i*grid_size), (screen.get_width(), i*grid_size))
            
    def draw_destination(self, destination, screen, circle_color):
        if self.debug_mode:
            pygame.draw.circle(screen, circle_color, (destination[0]*50 + 25, destination[1]*50 + 25), 10)