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
    screen.fill((255,255,255))
    
    game.collision_list.draw_collisions(screen)
    
    game.item_list.check_collision_and_add_item(game.joueur.body, game.joueur.destination)
    game.item_list.draw_items(screen)

    game.joueur.draw(screen)

    if game.debug.debug_mode:
        game.debug.draw(screen, game.joueur.body, game.joueur.destination, fps)

    
    if game.interface_craft.is_open:
        #on affiche l'UI pour le craft du perso
        game.interface_craft.draw_crafting_interface(screen)

 
    pygame.display.flip()


    if game.joueur.can_move:
            
        # Appliquer la gravité au joueur
        game.joueur.apply_gravity(dt, game.collision_list)

        if abs(game.joueur.pos[0] - game.joueur.destination[0]*50) < game.joueur.speed * dt * 1.5:
            game.joueur.pos[0] = game.joueur.destination[0]*50
            if game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d):
                game.joueur.move(1, game.collision_list)
            if game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q):
                game.joueur.move(-1, game.collision_list)
        else:
            game.joueur.update_pos(dt)


        if game.pressed.get(pygame.K_SPACE):
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
            game.interface_craft.click_up(pygame.mouse.get_pos())

    if game.pressed_down.get(pygame.K_e):
        #ouvrir ou fermer le menu de craft
        if game.interface_craft.is_open:
            game.interface_craft.close(game.joueur)
        else:
            game.interface_craft.open(game.joueur, game.collision_list)
    
    if game.pressed_down.get(pygame.K_F1):
        #active le mode debug
        game.debug.debug_mode = not game.debug.debug_mode

    if game.item_list.check_collision_and_add_item(game.joueur.body, game.joueur.destination):
        item = game.item_list.item_collected[-1]  # Dernier item collecté
        game.interface_craft.storage_case.drag_and_drop.set_item(item)
        game.interface_craft.open(game.joueur, game.collision_list)

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