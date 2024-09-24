import pygame
from games import Game

pygame.init()



#display gerer la fenetre de notre jeu
pygame.display.set_caption("test") 
screen = pygame.display.set_mode((1080, 720)) 

running = True 

#clock = pygame.time.Clock()

#charger notre jeu
game= Game()



while running:
    screen .fill((255,255,255))
    screen.blit(game.joueur.image, game.joueur.rect)


    if game.pressed.get(pygame.K_RIGHT) and game.joueur.rect.x + game.joueur.rect.width < screen.get_width():
        game.joueur.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.joueur.rect.x >0:
        game.joueur.move_left()
    
    #10    1014
    
    pygame.display.flip()
    
    #si le joueur ferme la fenhetre
    for event in pygame.event.get():
        #que l'evenhemenht est fermeture de fenhetre
        if event.type == pygame.QUIT:
           running = False 
           pygame.quit() 

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type ==pygame.KEYUP:
            game.pressed[event.key] =False
                

    
           
        



