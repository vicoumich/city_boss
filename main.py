import pygame
from jeu import Game
from menu import Menu
pygame.init()



#Générer fenêtre et changer nom et taille
pygame.display.set_caption("City Boss")
root_page = pygame.display.set_mode((1280,720))
running = True
jeu = Game()
menu = Menu()
background = menu.image
clock = pygame.time.Clock()

#mise en place des bouton est de leurs rectangles
button_bot = menu.button_bot
button_bot_rect = button_bot.get_rect()
button_bot_rect.x, button_bot_rect.y = 500, 230

button_pvp = menu.button_pvp
button_pvp_rect = button_pvp.get_rect()
button_pvp_rect.x, button_pvp_rect.y = 500, 350  

title = menu.title

#mise en place du bouton retour 
retour = pygame.image.load("pic/retour.png")
retour_rect = retour.get_rect()
retour_rect.x, retour_rect.y = -80, -70
count = 0
count2 = 0

#boucle du jeu tant que le jeu run
while running:
    count += 1
    count2 += 1

    #mise en place du fond et de la flèche de retour car ils seront la de partout
    root_page.blit(background, (0, 0))
    root_page.blit(retour, (retour_rect.x, retour_rect.y))
    
    # Déplacement des projectiles
    for x in jeu.player1.group_projectiles:
        x.move()
        
    for x in jeu.bot.group_projectiles:
        x.move()

    #lancement d'une partie 
    if jeu.is_playing:
        jeu.start(root_page)
    else:
        menu.maj_bg()
        background = menu.image
        root_page.blit(button_bot, (500, 230))
        root_page.blit(button_pvp, (500, 350))
        root_page.blit(title, (300, -50))
        
    # Bot tire
    if count2 > 500:
        count2 = 0
        jeu.bot.attaque()
    
    #refresh de root_page
    pygame.display.flip()
    #récupérer accion du joueur
    for event in pygame.event.get():

       #quitter
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
        
        #touche enfoncé ?
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True

            if event.key == pygame.K_SPACE and count > 180:
                jeu.player1.attaque()
                count = 0
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False
        
        #Si il y a un clique de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_bot_rect.collidepoint(event.pos):
                background = jeu.image
                jeu.is_playing = True 
            
            if retour_rect.collidepoint(event.pos):
                jeu = Game()
    clock.tick(80)
