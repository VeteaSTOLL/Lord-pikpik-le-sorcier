import pygame

class case():
    def __init__(self, i, j, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = (255,255,255)
        self.element = 0

        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, body):
        self.element = body[self.j][self.i]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.element != 0:            
            pygame.draw.rect(screen, (0,0,0), self.rect)

    def click(self, body, coords, collision_list, is_left_click):
        if is_left_click:
            if not collision_list.check_collision((coords[0] + self.i, coords[1] + self.j)):
                #vérifier si il y a des cases occupées adjacentes
                self.element = 1
        else:
            #vérifier si il y a au moins 2 cases occupées + si toutes les cases adjacentes ont un autre support
            self.element = 0
        body[self.j][self.i] = self.element
    


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

    def click(self, mouse_pos, body, coords, collision_list, is_left_click):        
        for case in self.cases:
            if case.x <= mouse_pos[0] and mouse_pos[0] <= case.x + case.width and case.y <= mouse_pos[1] and mouse_pos[1] <= case.y + case.height:
                case.click(body, coords, collision_list, is_left_click)
                return