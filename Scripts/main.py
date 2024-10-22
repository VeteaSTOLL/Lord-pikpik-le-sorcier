import pygame
from games import Game

pygame.init()
clock = pygame.time.Clock()


#display gerer la fenetre de notre jeu
pygame.display.set_caption("Bouboule") 
screen = pygame.display.set_mode((1000, 750)) 

running = True 



#charger notre jeu
game= Game()

while running:

    dt = clock.tick() / 1000.0
    fps = clock.get_fps()
    if fps != 0 :
        dt = 1 / fps    

    #affichage
    screen .fill((255,255,255))
    screen.blit(game.joueur.image, game.joueur.rect)
    
    game.collision_list.draw_collisions(screen)
    
    game.item_list.check_collision_and_add_item(game.joueur.rect)
    game.item_list.draw_items(screen)


    if game.debug.debug_mode:
        game.debug.draw_grid(screen, (255,0,0), 50)
        game.debug.draw_destination(game.joueur.destination, screen, (255,0,0))


    if game.crafting_interface:
        #on affiche l'UI pour le craft du perso
        #pygame.draw.rect(screen, (100,100,100),  pygame.Rect(30, 30, screen.get_width()-60, screen.get_height()-60))
        #game.item_list.draw_items_collected(screen)
        game.crafting_interface = game.interface_craft
        game.crafting_interface.draw_crafting_interface(screen, game.item_list)
        print("AVENGERSS")

        
        
    pygame.display.flip()

    # Appliquer la gravité au joueur
    game.joueur.apply_gravity(dt, game.collision_list)

    if abs(game.joueur.pos[0] - game.joueur.destination[0]*50) < game.joueur.speed * dt * 1.5:
        game.joueur.pos[0] = game.joueur.destination[0]*50
        game.joueur.rect.x = game.joueur.pos[0]
        if game.pressed.get(pygame.K_RIGHT):
            game.joueur.move(1, game.collision_list)
        if game.pressed.get(pygame.K_LEFT):
            game.joueur.move(-1, game.collision_list)
    else:
        game.joueur.update_pos(dt)

    if game.pressed.get(pygame.K_SPACE):
        game.joueur.jump()
    # Sauter si la touche Espace est pressée

    if game.pressed_down.get(pygame.K_e):
        #ouvrir le menu de craft
        game.crafting_interface = not game.crafting_interface
    if game.pressed_down.get(pygame.K_F1):
        #active le mode debug
        game.debug.debug_mode = not game.debug.debug_mode

    game.pressed_down = {}
    game.pressed_up = {}
    
    for event in pygame.event.get():
        #si le joueur ferme la fenetre
        if event.type == pygame.QUIT:
           running = False 
           pygame.quit() 

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            game.pressed_down[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] =False
            game.pressed_up[event.key] = True
