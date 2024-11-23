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
            game.pressed["clic_souris"] = True
            game.pressed_down["clic_souris"] = True
        if event.type == pygame.MOUSEBUTTONUP:
            game.pressed["clic_souris"] = False
            game.pressed_up["clic_souris"] = True


    if not game.interface_craft.is_open:
        # Appliquer la gravité au joueur
        game.joueur.apply_gravity(dt, game.collision_list)
        game.joueur.update_movement(game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q), game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d), dt, game.collision_list)

        if game.pressed.get(pygame.K_SPACE):
            if game.joueur.can_jump:
                game.joueur.jump()
        # Sauter si la touche Espace est pressée

    if game.pressed_down.get("clic_souris"):
        if game.interface_craft.is_open:
            game.interface_craft.click_down(pygame.mouse.get_pos())
    if game.pressed.get("clic_souris"):
        if game.interface_craft.is_open:
            game.interface_craft.click(pygame.mouse.get_pos(), game.joueur.body)
    if game.pressed_up.get("clic_souris"):
        if game.interface_craft.is_open:
            game.interface_craft.click_up(pygame.mouse.get_pos(), game.joueur.body)

    if game.pressed_down.get(pygame.K_e):
        #ouvrir ou fermer le menu de craft
        if game.interface_craft.is_open:
            if game.joueur.is_body_valid():
                game.interface_craft.close()
        else:            
            object = game.item_manager.check_collision(game.joueur.body, game.joueur.destination)
            game.interface_craft.open(game.joueur, game.collision_list, object)
    
    if game.pressed_down.get(pygame.K_F1):
        #active le mode debug
        game.debug.debug_mode = not game.debug.debug_mode    

    
    #affichage
    screen.fill((255,255,255))
    
    game.item_manager.draw_objects(screen)

    game.joueur.draw(screen, game.item_manager.item_types)

    game.collision_list.draw_collisions(screen)    

    if game.debug.debug_mode:
        game.debug.draw(screen, game.joueur.body, game.joueur.destination, fps, game.joueur.direction)

    
    if game.interface_craft.is_open:
        #on affiche l'UI pour le craft du perso
        game.interface_craft.draw_crafting_interface(screen)

 
    pygame.display.flip()
        
        