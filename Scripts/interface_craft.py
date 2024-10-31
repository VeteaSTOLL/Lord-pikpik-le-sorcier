from collections.abc import Iterable
import pygame

class case():
    def __init__(self, i, j, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (255,255,255)
        self.element = 0
        self.i = i
        self.j = j

    def update(self, body):
        self.element = body[self.j][self.i]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.element != 0:            
            pygame.draw.rect(screen, (0,0,0), self.rect)
    







class Interface_Craft():
    def __init__(self, screen_width, screen_height):
        self.base_width = 800
        self.base_height = 600
        self.base_color = (200, 200, 200)
        self.base_offset = ((screen_width-self.base_width)/2, (screen_height-self.base_height)/2)
        
        self.craft_width = 500
        self.craft_height = 500
        self.craft_color = (100, 100, 100)
        self.craft_offset = ((screen_width-self.craft_width)/2, (screen_height-self.craft_height)/2)

        self.size = 5
        self.space = 10

        self.case_width = (self.craft_width-self.space*(self.size+1))/self.size
        self.case_height = (self.craft_height-self.space*(self.size+1))/self.size

        self.cases = []
        
        for j in range(self.size):
            for i in range(self.size):
                self.cases.append(case(i, j, self.craft_offset[0] + (self.space + self.case_width) * i + self.space, self.craft_offset[1] + (self.space + self.case_height) * j + self.space, self.case_width, self.case_height))


    def draw_crafting_interface(self, screen):
        base = pygame.Rect(self.base_offset[0], self.base_offset[1], self.base_width, self.base_height)
        pygame.draw.rect(screen, self.base_color, base)
        
        craft = pygame.Rect(self.craft_offset[0], self.craft_offset[1], self.craft_width, self.craft_height)
        pygame.draw.rect(screen, self.craft_color, craft)

        for case in self.cases:
            case.draw(screen)

    def update(self, body):
        for case in self.cases:
            case.update(body)