import pygame

class case():
    def __init__(self, i, j, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)

        
        self.body_color = (0,0,0)
        self.void_color = (255,255,255)
        self.collision_color = (200,150,150)

        self.color = self.void_color

        self.element = 0
        self.in_collision = False

        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, body, coordimport pygame

class case():
    def __init__(self, i, j, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)

        
        self.body_color = (0,0,0)
        self.void_color = (255,255,255)
        self.collision_color = (200,150,150)

        self.color = self.void_color

        self.element = 0
        self.in_collision = False

        self.i = i
        self.j = j
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, body, coords, collision_list):
        self.element = body[self.j][self.i]
        self.in_collision = collision_list.check_collision((coords[0] + self.i, coords[1] + self.j))
        self.update_color()

    def update_color(self):        
        if self.in_collision:
            self.color = self.collision_color
        elif self.element != 0:
            self.color = self.body_color
        else:
            self.color = self.void_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


    def click(self, body, set):
        if set:
            if not self.in_collision:
                self.element = 1
        else:
            self.element = 0

        body[self.j][self.i] = self.element        
        
        self.update_color()

    # @staticmethod
    # def check_neighboring_body_parts(body, i, j):
    #     if i > 0 and body[j][i-1] == 1:
    #         return True
    #     if i < len(body)-1 and body[j][i+1] == 1:
    #         return True
    #     if j > 0 and body[j-1][i] == 1:
    #         return True
    #     if j < len(body[0])-1 and body[j+1][i] == 1:
    #         return True
    #     return False
    


class tool():
    def __init__(self, name, x, y, width, height, selected, image_path):
        self.rect = pygame.Rect(x,y,width,height)
        
        self.base_color = (100,100,100)
        self.selected_color = (255,255,255)

        self.color = self.base_color
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.name = name
        self.selected = selected
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.update_color()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, self.rect)

    def update_color(self):        
        if self.selected:
            self.color = self.selected_color
        else:
            self.color = self.base_color

    def select(self, s):
        self.selected = s
        self.update_color()



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

        self.tool_width = 100
        self.tool_height = 100
        self.tool_offset = (self.base_offset[0] + (self.craft_offset[0] - self.base_offset[0] - self.tool_width)/2, self.base_offset[1] + (self.base_height-(2*self.tool_height+self.space))/2)

        self.cases = []
        
        for j in range(self.size):
            ligne = []
            for i in range(self.size):
                ligne.append(case(i, j, self.craft_offset[0] + (self.space + self.case_width) * i + self.space, self.craft_offset[1] + (self.space + self.case_height) * j + self.space, self.case_width, self.case_height))
            self.cases.append(ligne)
        
        self.tools = []

        self.tools.append(tool("pinceau",self.tool_offset[0], self.tool_offset[1], self.tool_width, self.tool_height, True, "img/pinceau.png"))
        self.tools.append(tool("gomme",self.tool_offset[0], self.tool_offset[1] + self.tool_height + self.space, self.tool_width, self.tool_height, False,"img/gomme.png"))

        self.selected_tool = "pinceau"


    def draw_crafting_interface(self, screen):
        base = pygame.Rect(self.base_offset[0], self.base_offset[1], self.base_width, self.base_height)
        pygame.draw.rect(screen, self.base_color, base)
        
        craft = pygame.Rect(self.craft_offset[0], self.craft_offset[1], self.craft_width, self.craft_height)
        pygame.draw.rect(screen, self.craft_color, craft)

        for ligne in self.cases:
            for case in ligne:
                case.draw(screen)
        
        for t in self.tools:
            t.draw(screen)

                
    def event(self, event):
        # Passe 'self' comme tool_manager lors de l'appel de `event()` dans les cases
        for case in self.cases:
            case.event(event, self)
        for tool_item in self.tools:
            tool_item.event(event, self)
    
    def update(self, body, coords, collision_list):
        for ligne in self.cases:
            for case in ligne:
                case.update(body, coords, collision_list)

    def click(self, mouse_pos, body): 
        for ligne in self.cases:
            if ligne[0].y <= mouse_pos[1] and mouse_pos[1] <= ligne[0].y + self.case_height:
                for case in ligne:
                    if case.x <= mouse_pos[0] and mouse_pos[0] <= case.x + self.case_width:
                        case.click(body, self.selected_tool == "pinceau")
                        return
                    
        for t in self.tools:
            if (t.x <= mouse_pos[0] and mouse_pos[0] <= t.x + t.width) and (t.y <= mouse_pos[1] and mouse_pos[1] <= t.y + t.height):
                for t2 in self.tools:
                    t2.select(False)
                t.select(True)
                self.selected_tool = t.name 
    


class stock_item_case:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None
        self.stock_item_case_name = None
        self.drag = False 
        self.mouse_offset = (0, 0) 

    def update_stock_item_case(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), self.rect)
        if self.image:
            screen.blit(self.image, self.rect)
            
