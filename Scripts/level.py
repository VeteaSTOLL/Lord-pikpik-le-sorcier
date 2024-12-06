# niveau.py
from collisions import collision_list, collision
from objets import item, object

class Level:
    def __init__(self, collisions_element, objets_element):

        self.collisions = collision_list()
        for element in collisions_element:
            self.collisions.collisions.append(collision(*element))

        self.objects = []
        for element in objets_element:
            self.objects.append(object(*element))

    def get_collisions(self):
        return self.collisions

    def get_objects(self):
        return self.objects
    
    
