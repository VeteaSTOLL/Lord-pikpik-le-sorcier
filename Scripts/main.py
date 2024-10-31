import pygame
from games import Game

pygame.init()
clock = pygame.time.Clock()


#display gerer la fenetre de notre jeu
pygame.display.set_caption("Bouboule") 
screen = pygame.display.set_mode((1000, 750)) 

running = True 



#charger notre jeu
game= Game(screen)

while running:
    #permet de renseigner la variable "dt" qui est le différentiel de temps entre l'avant dernière frame et la dernière frame, prartique pour pouvoir rendre le gameplay indépendant du framerate
    dt = clock.tick() / 1000.0
    fps = clock.get_fps()
    if fps != 0 :
        dt = 1 / fps    

    #affichage
    screen .fill((255,255,255))
    
    game.collision_list.draw_collisions(screen)
    
    game.item_list.check_collision_and_add_item(game.joueur.body, game.joueur.destination)
    game.item_list.draw_items(screen)

    game.joueur.draw(screen)

    if game.debug.debug_mode:
        game.debug.draw_grid(screen, (255,0,0), 50)
        game.debug.draw_destination(game.joueur.destination, game.joueur.body, screen, (255,0,0))
        game.debug.draw_infos(screen, fps, game.joueur.destination)


    if game.crafting_interface_is_open:
        #on affiche l'UI pour le craft du perso
        game.interface_craft.draw_crafting_interface(screen)
 
    pygame.display.flip()


    if game.joueur.can_move:
        
        # Appliquer la gravité au joueur
        game.joueur.apply_gravity(dt, game.collision_list)

        if abs(game.joueur.pos[0] - game.joueur.destination[0]*50) < game.joueur.speed * dt * 1.5:
            game.joueur.pos[0] = game.joueur.destination[0]*50
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
        game.crafting_interface_is_open = not game.crafting_interface_is_open
        if game.crafting_interface_is_open:
            game.interface_craft.update(game.joueur.body)
        game.joueur.can_move = not game.crafting_interface_is_open
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

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            game.pressed_down[event.key] = True
        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            game.pressed_up[event.key] = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.interface_craft.click(pygame.mouse.get_pos(), game.joueur.body, game.joueur.destination, game.collision_list, event.button == 1)
