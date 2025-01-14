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
        self.body_color = (50,255,220)
        self.object_color = (255,255,255)
        self.void_color = (255,255,255)
        self.collision_color = (50,50,50)
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

    def paint(self, body, set, son_pinceau, son_gomme):
        if set:
            if self.element == 0:
                self.set_element(body, 1, son_pinceau)
        else:
            if self.element == 1:
                self.set_element(body, 0, son_gomme)
    
    def set_element(self, body, element, sound=None):
        if not self.in_collision:
            self.element = element
            body[self.j][self.i] = self.element
            self.update_color()
            if sound != None:
                pygame.mixer.Sound.play(sound)
        
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

        self.show_connectivity_lines = False
        self.lines = [[(x,y), (x+width,y)], [(x+width,y), (x+width,y+height)], [(x+width,y+height), (x,y+height)], [(x,y+height), (x,y)]]

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
        self.show_connectivity_lines = False
        self.reset_image_coords()
    
    def reset_image_coords(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        if self.item != None and self.show_connectivity_lines:
            for i in range(4):
                if self.item.connectivity[i]:
                    start = (self.lines[i][0][0] + (self.rect.x - self.x), self.lines[i][0][1] + (self.rect.y - self.y))
                    end = (self.lines[i][1][0] + (self.rect.x - self.x), self.lines[i][1][1] + (self.rect.y - self.y))
                    pygame.draw.line(screen, (255,50,50), start, end, width=3)


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

        self.error = ""
        self.font = pygame.font.SysFont('arial', 30)


        self.son_pinceau = pygame.mixer.Sound("sounds/pinceau.wav")
        self.son_gomme = pygame.mixer.Sound("sounds/gomme.wav")
        self.son_erreur = pygame.mixer.Sound("sounds/erreur.wav")

    def open(self, joueur, collision_list, object=None):        
        self.update(joueur.body, joueur.destination, collision_list)
        if object != None:
            self.storage_case.drag_and_drop.set_item(object.item)
            self.object = object
        self.error = ""
        self.is_open = True
        pygame.mixer.music.pause()
    
    def close(self, error):
        if error == "":
            self.is_open = False
            if self.object != None and self.storage_case.drag_and_drop.item == None:
                self.object.collect()
            
            self.object = None
            self.storage_case.drag_and_drop.clear()
            self.show_items_connectivity(False)
            pygame.mixer.music.unpause()
        else:            
            pygame.mixer.Sound.play(self.son_erreur)
            self.error = error
            if error == "Item(s) mal placé(s)":
                self.show_items_connectivity(True)

    def show_items_connectivity(self, b):
        for ligne in self.cases:
            for case in ligne:
                if case.drag_and_drop.item != None or not b:
                    case.drag_and_drop.show_connectivity_lines = b

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
        
        text = self.font.render(self.error, False, (255, 50, 50))
        screen.blit(text, ((screen.get_width()-text.get_width())/2, self.base.y - text.get_height()))
    
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
                        case.paint(body, self.selected_tool == "pinceau", self.son_pinceau, self.son_gomme)
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
                            pygame.mixer.Sound.play(self.son_pinceau)

            self.item_origin.reset_image_coords()
            self.holded_item = None
            self.item_origin = None

            for ligne in self.cases:
                for case in ligne:
                    case.update_element(body)

    
    def reset_interface(self):
           
        for ligne in self.cases:
            for case in ligne:
                case.set_element(body= [[0]*self.size for _ in range(self.size)] , element=0)
                case.drag_and_drop.clear()

        for t in self.tools:
            t.select(False)
        self.tools[0].select(True)  
        self.selected_tool = "pinceau"

        self.storage_case.drag_and_drop.clear()
        self.storage_case.reset_drag_and_drop_coords()
        self.object = None

        self.error = ""

        self.holded_item = None
        self.item_origin = None

        self.show_items_connectivity(False)
        self.is_open = False

class Interface_Item_Discovery():
    def __init__(self, screen_width, screen_height):
        self.is_open = False

        self.base = pannel(0, 0, 600, 400, (255, 255, 255))
        self.base.center(0, 0, screen_width, screen_height)
        
        self.item_frame = pygame.Rect((screen_width-100)/2,220,100,100)
        self.item_sprite = None

        self.item = None
        
        self.title_font = pygame.font.SysFont('arial', 30, bold=True)
        self.body_font = pygame.font.SysFont('arial', 20)

        self.item_name_render = None
        self.item_desciption_renders = []
        self.indication_render = self.body_font.render("Appuyer sur E pour fermer", False, (0, 0, 0))

    def open(self, item):
        self.item = item
        item.discovered = True

        self.item_sprite = item.image
        self.item_sprite = pygame.transform.scale(self.item_sprite, (100, 100))    
        
        self.item_name_render = self.title_font.render(item.name.upper(), False, (0, 0, 0))
        self.render_paragraph(item.description, 50, self.item_desciption_renders)

        self.is_open = True
    
    def close(self):
        self.is_open = False
        self.item_name_render = []
        self.item_desciption_renders = []

    def render_paragraph(self, text, length, render_list):
        lines = []
        line = ""
        word = ""
        letters = 0
        for i in range(len(text)):
            if letters > length:
                lines.append(line)
                line = ""
                letters = 0

            if text[i] == " ":
                line += word + " "
                word = ""
            else:
                word += text[i]
            letters += 1

        line += word        
        lines.append(line)
        
        for l in lines:
            render_list.append(self.body_font.render(l, False, (0, 0, 0)))


    def draw(self, screen):
        self.base.draw(screen)
        if self.item != None:
            screen.blit(self.item_sprite, self.item_frame)
            screen.blit(self.item_name_render, ((screen.get_width()-self.item_name_render.get_width())/2, 330))
            for i in range(len(self.item_desciption_renders)):
                render = self.item_desciption_renders[i]
                screen.blit(render, ((screen.get_width()-render.get_width())/2, 400 + i * 20))
        screen.blit(self.indication_render, ((screen.get_width()-self.indication_render.get_width())/2, 540))