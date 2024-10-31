import pygame 

class item ():
    def __init__(self, name, image_path, x, y, dx, dy):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (dx * 50, dy * 50))
        self.position = [x,y]
        self.size = [dx,dy]
        self.rect = pygame.Rect(self.position[0] * 50, self.position[1] * 50, self.size[0] * 50, self.size[1] * 50)
        self.collected = False
    
    def draw_item(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)


class item_list():
    def __init__(self):        
        self.items = []
        self.item_collected=[]

        self.items.append(item("roulette", "img/roulette.jpg", 12,13,1,1))
        self.items.append(item("bouboule", "img/rond_noir.png", 14,13,1,1))
        self.items.append(item("bouboule", "img/rond_noir.png", 16,13,1,1))
        
        
    def draw_items(self, screen):
        for i in self.items:
            i.draw_item(screen)
     
    def check_collision_and_add_item(self, body, coords):
        for item in self.items:
            if not item.collected:
                
                for i in range(5):
                    for j in range(5):
                        if body[i][j] != 0 and item.position == [coords[0] + j, coords[1] + i]:
                            self.item_collected.append(item)  
                            item.collected = True
                            
                            print(item.name)
            
    

