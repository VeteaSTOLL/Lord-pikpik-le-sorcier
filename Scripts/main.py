import pygame
from games import Game


pygame.init()
clock = pygame.time.Clock()


#display gerer la fenetre de notre jeu
pygame.display.set_caption("Bouboule") 
screen = pygame.display.set_mode((1000, 750)) 

running = True 
affiche_regle = True
start_game = False

#charger notre jeu
game = Game(screen)
current_level = 1
niveau = game.level_manager.creer_niveau(current_level)

game.collision_list = niveau.get_collisions()
game.item_manager.objects = niveau.get_objects()

font_title = pygame.font.Font(None, 48)
font_text = pygame.font.Font(None, 36)

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
            if affiche_regle and event.key ==   pygame.K_s: 
                    affiche_regle = False
                    start_game = True
        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            game.pressed_up[event.key] = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.pressed["clic_souris"] = True
            game.pressed_down["clic_souris"] = True
        if event.type == pygame.MOUSEBUTTONUP:
            game.pressed["clic_souris"] = False
            game.pressed_up["clic_souris"] = True
    
    if affiche_regle:
        screen.fill((135, 206, 250))

        regles = [
            " Lord PIKPIK le sorcier !",
            " ",
            "Résolvez tous les niveaux afin de finir le jeu.",
            "",
            "Touches :",
            "           * Vous déplacer avec les flèches et sauter avec la barre espace",
            "           * Appuyer sur E pour acceder à l'espace de craft",
            "           * Appuyer sur R pour recommencer le niveau",
            "",
            "",
            " Il est l'heure de commencer, appuyez sur S",
            "Amusez-vous !"
        ]
        titre = font_title.render(regles[0], True, (255,255,255))
        titre_rect = titre.get_rect(center=(1000 // 2, 100)) 
        screen.blit(titre, titre_rect)

        
        y_offset = 160  
        for ligne in regles[1:]:
            texte = font_text.render(ligne, True, (128, 128, 128))
            texte_rect = texte.get_rect(left=50, top=y_offset) 
            screen.blit(texte, texte_rect)
            y_offset += 40
   
    
    if current_level > game.level_manager.nb_level:
        running = False
    else:
        game.collision_list = niveau.get_collisions()
        game.item_manager.objects = niveau.get_objects()
    pygame.display.flip()


    if not game.interface_craft.is_open:
        # Appliquer la gravité au joueur
        game.joueur.apply_gravity(dt, game.collision_list)
        game.joueur.update_movement(game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q), game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d), dt, game.collision_list, game.item_manager)

        if game.pressed.get(pygame.K_SPACE):
            if game.joueur.can_jump:
                game.joueur.jump()
        # Sauter si la touche Espace est pressée


    if game.interface_craft.is_open and not game.interface_item_discovery.is_open:
        if game.pressed_down.get("clic_souris"):
            game.interface_craft.click_down(pygame.mouse.get_pos())
        if game.pressed.get("clic_souris"):
            game.interface_craft.click(pygame.mouse.get_pos(), game.joueur.body)
        if game.pressed_up.get("clic_souris"):
            game.interface_craft.click_up(pygame.mouse.get_pos(), game.joueur.body)

    if game.pressed_down.get(pygame.K_e):
        #ouvrir ou fermer le menu de craft
        if not game.interface_item_discovery.is_open:
            if game.interface_craft.is_open:
                error = game.joueur.is_body_valid(game.item_manager.item_types)
                game.interface_craft.close(error)
                game.joueur.check_for_item(game.item_manager)
            else:       
                object = game.item_manager.check_collision(game.joueur.body, game.joueur.destination)
                if object and object.item.name == "porte":
                    game.level_manager.door_sound.play()
                   
                    current_level += 1
                    niveau = game.level_manager.creer_niveau(current_level)
                    game.joueur.reset_body()
                    game.interface_craft.reset_interface()
                else:     
                    game.interface_craft.open(game.joueur, game.collision_list, object)
                    if object != None and not object.item.discovered:
                        game.interface_item_discovery.open(object.item)
        else:
            game.interface_item_discovery.close()
      
    if game.pressed_down.get(pygame.K_F1):
        #active le mode debug
        game.debug.debug_mode = not game.debug.debug_mode    

    if game.pressed_down.get(pygame.K_r):
        game.level_manager.game_over_sound.stop()
        niveau = game.level_manager.creer_niveau(current_level)
        game.joueur.reset_body()
        game.interface_craft.reset_interface()
    
    if not affiche_regle :
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
        if game.interface_item_discovery.is_open:
            game.interface_item_discovery.draw(screen)

        if  game.joueur.pos[1]>750 :
            #current_level = 1
            image = pygame.image.load("img/game_over.png")
            game.level_manager.game_over_sound.play()
            screen.fill((0, 0, 0))
            screen.blit(image,(0,0))
            
        
        pygame.display.flip()
        
        
      