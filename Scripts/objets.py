import pygame 

class item ():
    def __init__(self, name, id, image_path):
        self.name = name
        self.id = id
        self.image_path = image_path
        self.image = pygame.image.load(image_path) 

class object():
    def __init__(self, item, x, y, dx, dy):
        self.item = item
        item.image = pygame.transform.scale(item.image, (dx*50, dy*50))
                
        self.rect = pygame.Rect(x * 50, y * 50, dx * 50, dy * 50)
        self.position = [x, y]

        self.collected = False
    
    def draw_object(self, screen):
        if not self.collected:
            screen.blit(self.item.image, self.rect)
    
    def collect(self):
        self.collected = True


class item_manager():
    def __init__(self):
        self.roulette = item("roulette", 2, "img/roulette.png")
        self.botte = item("botte", 3, "img/botte.png")
        self.porte = item("porte", 4, "img/porte.jpg")

        self.item_types = [self.roulette, self.botte, self.porte]

        self.objects = []

        self.objects.append(object(self.roulette, 6,9,1,1))
        self.objects.append(object(self.roulette, 3,13,1,1))
        self.objects.append(object(self.botte, 4,13,1,1))
        self.objects.append(object(self.porte, 18,8,1,1))
        
        
    def draw_objects(self, screen):
        for o in self.objects:
            o.draw_object(screen)
     
    def check_collision(self, body, coords):
        for object in self.objects:
            if not object.collected:
                
                for i in range(5):
                    for j in range(5):
                        if body[i][j] != 0 and object.position == [coords[0] + j, coords[1] + i]:
                            return object
        return None
                        
    

