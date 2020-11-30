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
fps = 30

consignes_is_open = False

#mise en place des images sur le menu est de leurs rectangles
button_bot = menu.button_bot
button_bot_rect = button_bot.get_rect()
button_bot_rect.x, button_bot_rect.y = 500, 230

button_pvp = menu.button_pvp
button_pvp_rect = button_pvp.get_rect()
button_pvp_rect.x, button_pvp_rect.y = 500, 350  

button_consignes = menu.consignes
button_consignes_rect = button_consignes.get_rect()
button_consignes_rect.x, button_consignes_rect.y = 1150, 630

commandes = menu.commandes

title = menu.title

#mise en place du bouton retour 
retour = pygame.image.load("pic/retour.png")
retour_rect = retour.get_rect()
retour_rect.x, retour_rect.y = -80, -70

# Compteurs pour les attaques des personnages
count = 0
count2 = 0

# Boucle du jeu tant que le jeu run
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

    #lancement d'une partie contre un bot
    if jeu.is_playing == 'PVB':
        jeu.start(root_page)
        fps = 80

    # Lancement d'une partie contre un joeur sur le meme clavier
    elif jeu.is_playing == 'PVP':
        jeu.start_pvp(root_page)
        fps = 80

    # si le joueurs est en train de lire les relges
    elif consignes_is_open:
        menu.maj_bg()
        background = menu.image
        root_page.blit(commandes, (100, 50))

    # Chargement et affichages des images sur le menu
    else:
        menu.maj_bg()
        background = menu.image              # Animation du fond
        root_page.blit(button_bot, (500, 230))
        root_page.blit(button_pvp, (500, 350))
        root_page.blit(button_consignes, (1150, 630))
        root_page.blit(title, (300, -50))
        fps = 30     # Adapatation de fps pour l'animation
        
    # Bot tire
    if count2 > 500 and jeu.bot.is_bot:
        count2 = 0
        jeu.bot.attaque()
    
    #refresh de root_page
    pygame.display.flip()


    #récupérer accions du joueur et les parcourir
    for event in pygame.event.get():

       #quitter
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
        
        #touche enfoncé ?
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True   # Ajout de la touche accionnée en direct au dico pressed 
            # Attaque du joueur 1 si adversaire est un robot
            if event.key == pygame.K_SPACE and count > 160 and jeu.bot.is_bot:
                jeu.player1.attaque()
                count = 0
            
            # Action joueur deux (n'étant pas un robot)
            elif not jeu.bot.is_bot: 

                # Si joueur 1 appui sur M alors attaque
                if event.key == pygame.K_SEMICOLON and count > 100:
                    jeu.player1.attaque()
                    count = 0

                # Si joueur 2 appui sur espace alors attaque
                if event.key == pygame.K_SPACE and count2 > 100:
                    jeu.bot.attaque()
                    count2 = 0
                
                
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False
        
        #Si il y a un clique de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # Si le joueur clique sur un bouton du menu
            if button_bot_rect.collidepoint(event.pos):
                background = jeu.image
                jeu.is_playing = 'PVB' 
            
            if button_pvp_rect.collidepoint(event.pos):
                background = jeu.image
                jeu.is_playing = 'PVP'

            if button_consignes_rect.collidepoint(event.pos):
                consignes_is_open = True
            
            if retour_rect.collidepoint(event.pos):
                # Reinitialisation de la partie
                jeu = Game()
                consignes_is_open = False
    clock.tick(fps)
