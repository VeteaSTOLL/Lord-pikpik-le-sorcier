import pygame

class pannel():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = color

        self.rect = pygame.Rect(x,y,width,height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def center(self, x, y, width, height):
        self.x = (width - self.width) / 2 + x
        self.y = (height - self.height) / 2 + y
        self.update_rect()
        
    def center_to_pannel(self, pannel):
        self.center(pannel.x, pannel.y, pannel.width, pannel.height)

    def update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y

        self.rect.width = self.width
        self.rect.height = self.height

    def contain(self, coords):
        return (self.x <= coords[0] and coords[0] <= self.x + self.width) and (self.y <= coords[1] and coords[1] <= self.y + self.height)
    

class case():
    def __init__(self, i, j, x, y, width, height):
        self.body_color = (0,0,0)
        self.object_color = (200,250,200)
        self.void_color = (255,255,255)
        self.collision_color = (200,150,150)
        self.error_color = (255,0,255)

        self.pannel = pannel(x, y, width, height, self.void_color)
        self.drag_and_drop = drag_and_drop(x, y, width, height)

        self.element = 0
        self.in_collision = False

        self.i = i
        self.j = j

    def update_collision_detection(self, body, coords, collision_list):
        self.element = body[self.j][self.i]
        self.in_collision = collision_list.check_collision((coords[0] + self.i, coords[1] + self.j))
        self.update_color()

    def update_color(self):
        if self.in_collision:
            self.pannel.color = self.collision_color
        elif self.element == 0:
            self.pannel.color = self.void_color
        elif self.element == 1:
            self.pannel.color = self.body_color
        elif self.element >= 2:
            self.pannel.color = self.object_color
        else :
            self.pannel.color = self.error_color

    def update_element(self, body):
        if self.drag_and_drop.item == None:
            if self.element >= 2:
                self.set_element(body, 0)
        else:
            self.set_element(body, self.drag_and_drop.item.id)

    def paint(self, body, set):
        if set:
            if self.element == 0:
                self.set_element(body, 1)
        else:
            if self.element == 1:
                self.set_element(body, 0)
    
    def set_element(self, body, element):
        if not self.in_collision:
            self.element = element
            body[self.j][self.i] = self.element
            self.update_color()
        
    def draw(self, screen):
        self.pannel.draw(screen)



class tool():
    def __init__(self, name, x, y, width, height, selected, image_path):
        self.base_color = (100,100,100)
        self.selected_color = (255,255,255)
        
        self.pannel = pannel(x, y, width, height, self.base_color)
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.name = name
        self.selected = selected

        self.update_color()

    def draw(self, screen):
        self.pannel.draw(screen)
        screen.blit(self.image, self.pannel.rect)

    def update_color(self):        
        if self.selected:
            self.pannel.color = self.selected_color
        else:
            self.pannel.color = self.base_color

    def select(self, s):
        self.selected = s
        self.update_color()

class stock_item_case():
    def __init__(self, x, y, width, height):
        self.pannel = pannel(x, y, width, height, (150, 150, 150))
        self.drag_and_drop = drag_and_drop(x, y, width, height)

    def draw(self, screen):
        self.pannel.draw(screen)
        self.drag_and_drop.draw(screen)

    def reset_drag_and_drop_coords(self):
        self.drag_and_drop.x = self.pannel.x
        self.drag_and_drop.y = self.pannel.y
        self.drag_and_drop.reset_image_coords()

class drag_and_drop():
    def __init__(self, x, y, width, height):
        self.item = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        self.image = None

    def set_item(self, item):
        if item != None:
            self.item = item
            self.image = pygame.image.load(item.image_path)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def set_image_coords(self, x, y):        
        self.rect.x = x
        self.rect.y = y
        
    def clear(self):
        self.item = None
        self.image = None
        self.reset_image_coords()
    
    def reset_image_coords(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)


class Interface_Craft():
    def __init__(self, screen_width, screen_height):
        self.is_open = False

        self.base = pannel(0, 0, 800, 600, (200, 200, 200))
        self.base.center(0, 0, screen_width, screen_height)
        
        self.craft = pannel(0, 0, 500, 500, (100, 100, 100))
        self.craft.center_to_pannel(self.base)

        self.size = 5
        self.space = 10

        self.case_width = (self.craft.width-self.space*(self.size+1))/self.size
        self.case_height = (self.craft.height-self.space*(self.size+1))/self.size

        self.tool_width = 100
        self.tool_height = 100
        self.tool_offset = (self.base.x + (self.craft.x - self.base.x - self.tool_width)/2, self.base.y + (self.base.height-(2*self.tool_height+self.space))/2)

        self.cases = []
        
        for j in range(self.size):
            ligne = []
            for i in range(self.size):
                ligne.append(case(i, j, self.craft.x + (self.space + self.case_width) * i + self.space, self.craft.y + (self.space + self.case_height) * j + self.space, self.case_width, self.case_height))
            self.cases.append(ligne)
        
        self.tools = []

        self.tools.append(tool("pinceau",self.tool_offset[0], self.tool_offset[1], self.tool_width, self.tool_height, True, "img/pinceau.png"))
        self.tools.append(tool("gomme",self.tool_offset[0], self.tool_offset[1] + self.tool_height + self.space, self.tool_width, self.tool_height, False,"img/gomme.png"))

        self.selected_tool = "pinceau"
        
        self.storage_case = stock_item_case(0, 0, 100, 100)
        self.storage_case.pannel.center(self.craft.x+self.craft.width, self.base.y, (self.base.width-self.craft.width)/2, self.base.height)
        self.storage_case.reset_drag_and_drop_coords()

        self.object = None

        self.holded_item = None
        self.item_origin = None

    def open(self, joueur, collision_list, object=None):        
        self.update(joueur.body, joueur.destination, collision_list)
        if object != None:
            self.storage_case.drag_and_drop.set_item(object.item)
            self.object = object
        joueur.can_move = False           
        self.is_open = True
    
    def close(self, joueur):
        #vérifier la former du perso avant de fermer
        joueur.can_move = True
        self.is_open = False
        if self.object != None and self.storage_case.drag_and_drop.item == None:
            self.object.collect()
        
        self.object = None
        self.storage_case.drag_and_drop.clear()

    def draw_crafting_interface(self, screen):
        self.base.draw(screen)        
        self.craft.draw(screen)

        for ligne in self.cases:
            for case in ligne:
                case.draw(screen)
        
        for t in self.tools:
            t.draw(screen)

        self.storage_case.draw(screen)
        
        for ligne in self.cases:
            for case in ligne:
                case.drag_and_drop.draw(screen)
    
    def update(self, body, coords, collision_list):
        for ligne in self.cases:
            for case in ligne:
                case.update_collision_detection(body, coords, collision_list)

    def take_item(self, drag_and_drop):
        self.holded_item = drag_and_drop.item
        self.item_origin = drag_and_drop

    def click(self, mouse_pos, body):
        if self.holded_item != None:
            self.item_origin.set_image_coords(mouse_pos[0] - 50, mouse_pos[1] - 50)
        else:
            for ligne in self.cases:
                for case in ligne:
                    if case.pannel.contain(mouse_pos):
                        case.paint(body, self.selected_tool == "pinceau")
                        return
                        
            for t in self.tools:
                if t.pannel.contain(mouse_pos):
                    for t2 in self.tools:
                        t2.select(False)
                    t.select(True)
                    self.selected_tool = t.name
        
    def click_down(self, mouse_pos):
        if self.storage_case.pannel.contain(mouse_pos):
            self.take_item(self.storage_case.drag_and_drop)

        for ligne in self.cases:
            for case in ligne:
                if case.pannel.contain(mouse_pos) and case.drag_and_drop.item != None:
                    self.take_item(case.drag_and_drop)


    def click_up(self, mouse_pos, body):
        if self.holded_item:

            if self.storage_case.pannel.contain(mouse_pos) and self.object != None:
                self.item_origin.clear()
                self.storage_case.drag_and_drop.set_item(self.holded_item)
            else:
                for ligne in self.cases:
                    for case in ligne:
                        if case.pannel.contain(mouse_pos) and not case.in_collision and case.element == 0:
                            self.item_origin.clear()
                            case.drag_and_drop.set_item(self.holded_item)
            

            self.item_origin.reset_image_coords()
            self.holded_item = None
            self.item_origin = None

            for ligne in self.cases:
                for case in ligne:
                    case.update_element(body)