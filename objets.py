import pygame 

class item ():
    def __init__(self, name, image_path, x, y,dx,dy):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (dx * 50, dy * 50))
        self.position = [x,y]
        self.size = [dx,dy]
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0] * 50, self.size[1] * 50)
        self.not_collected = True
        
        
        
    def draw_item(self, screen):
        if self.not_collected:
            screen.blit(self.image, self.rect)


class item_list():
    def __init__(self):        
        self.item = []
        self.item_collected=[]

        self.item.append(item("roulette", "img/roulette.jpg", 600,650,1,1))
        self.item.append(item("bouboule", "img/rond_noir.png", 700,650,1,1))
        self.item.append(item("bouboule", "img/rond_noir.png", 800,650,1,1))
        
    def draw_items(self, screen):
        for i in self.item:
            i.draw_item(screen)
    

    def draw_items_collected(self, screen):
        for item in self.item_collected:
            if item.not_collected: 
                item.draw_item(screen)

 
    def check_collision_and_add_item(self, coords):
      for item in self.item:
        if item.not_collected and item.rect.colliderect(coords):
            self.item_collected.append(item)  
            item.not_collected = False
            
            print("AVENGERSS")
            print(item.name)
            print("AVENGERSS")
    
    

