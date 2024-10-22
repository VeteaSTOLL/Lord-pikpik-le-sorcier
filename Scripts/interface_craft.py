import pygame

class Interface_Craft():

    def draw_crafting_interface(self, screen, item_list):
        craft_interface_rect = pygame.Rect(30, 30, screen.get_width()-60, screen.get_height()-60)
        
        pygame.draw.rect(screen, (253, 176, 170), craft_interface_rect)

        colones = 6
        lignes = 1
        item_boxe_size = 50
        space = 5

        for row in range(lignes):
            for col in range(colones):
                x = craft_interface_rect.x + craft_interface_rect.width*1/2 + col * (item_boxe_size + space) 
                
                y = craft_interface_rect.y+ craft_interface_rect.height -60 + row * (item_boxe_size + space)
                
                pygame.draw.rect(screen, (255, 255, 0), (x, y, item_boxe_size, item_boxe_size), 3)

                index_item = row *colones + col #calcule index par rapport a pos case dans grille.
                if index_item < len(item_list.item_collected):
                    item = item_list.item_collected[index_item]
                    screen.blit(item.image, (x, y))
