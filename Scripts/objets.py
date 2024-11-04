import pygame 

class item ():
    def __init__(self, name, image_path, x, y, dx, dy):
        self.name = name
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50,50))
                
        self.rect = pygame.Rect(x * 50, y * 50, dx * 50, dy * 50)
        self.position = [x, y]


        self.collected = False
    
    def draw_item(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)


class item_list():
    def __init__(self):        
        self.items = []

        self.items.append(item("roulette", "img/roulette.jpg", 6,9,1,1))
        self.items.append(item("roulette", "img/roulette.jpg", 10,13,1,1))
        self.items.append(item("botte", "img/botte.jpg", 4,13,1,1))
        self.items.append(item("porte", "img/porte.jpg", 18,8,1,1))
        
        
    def draw_items(self, screen):
        for i in self.items:
            i.draw_item(screen)
     
    def check_collision_and_add_item(self, body, coords):
        for item in self.items:
            if not item.collected:
                
                for i in range(5):
                    for j in range(5):
                        if body[i][j] != 0 and item.position == [coords[0] + j, coords[1] + i]:
                            item.collected = True
                        
                            return item
    



