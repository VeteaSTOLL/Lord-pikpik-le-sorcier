import pygame
from games import Game
from platformClass import Platform

pygame.init()
clock = pygame.time.Clock()


#display gerer la fenetre de notre jeu
pygame.display.set_caption("test") 
screen = pygame.display.set_mode((1000, 750)) 

running = True 

#clock = pygame.time.Clock()

#charger notre jeu
game= Game()

while running:
    # On obtient le differentiel de temps entre la dernière frame et l'avant dernière frame : utile pour rendre le gameplay indépendant du framerate.
    dt = clock.tick() / 1000.0
    fps = clock.get_fps()
    if fps != 0 :
        dt = 1 / fps    

    #affichage
    screen .fill((255,255,255))
    screen.blit(game.joueur.image, game.joueur.rect)
    screen.blit(game.roulette.image, game.roulette.rect)
    game.display_platforms(screen)
    game.debug.draw_grid(screen, (255,0,0), 50)
    game.debug.draw_destination(game.joueur.destination, screen, (255,0,0))

    if game.crafting_interface:
        #on affiche l'UI pour le craft du perso
        pygame.draw.rect(screen, (100,100,100), pygame.Rect(30, 30, screen.get_width()-60, screen.get_height()-60))

    pygame.display.flip()


    # Appliquer la gravité au joueur
    game.joueur.apply_gravity(dt)
    # Vérifier les collisions du joueur avec les plateformes
    game.check_collisions()



    if game.pressed.get(pygame.K_RIGHT) and game.joueur.rect.x + game.joueur.rect.width < screen.get_width():
        game.joueur.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.joueur.rect.x >0:
        game.joueur.move_left()
    if game.pressed.get(pygame.K_SPACE):
        game.joueur.jump()
    # Sauter si la touche Espace est pressée
    game.joueur.move(dt)

    if game.pressed_down.get(pygame.K_e):
        #ouvrir le menu de craft
        game.crafting_interface = not game.crafting_interface
    if game.pressed_down.get(pygame.K_F1):
        #active le mode debug
        game.debug.debug_mode = not game.debug.debug_mode

    
    
    #10    1014
    
    

    game.pressed_down = {}
    game.pressed_up = {}
    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
           running = False 
           pygame.quit() 

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            game.pressed_down[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] =False
            game.pressed_up[event.key] = True
            

        
                

    
           
        
