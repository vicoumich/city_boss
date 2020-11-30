import pygame

class Menu():
    def __init__(self):
        self.menu_images = []

        # Chargement des 128 images de l'animation dans la liste menu_images
        for x in range(1, 128):
            self.menu_images.append(pygame.transform.scale(pygame.image.load("pic/menu/f ({}).gif".format(str(x))), (1280,720)))
        
        self.image = self.menu_images[0]
        self.index = 0

        # Charement des images suplemntaires
        # Fonction scale redimensionne
        self.button_bot = pygame.image.load("pic/button_bot.png")
        self.button_pvp = pygame.image.load("pic/button_pvp.png")
        self.title = pygame.image.load("pic/title.png")
        self.consignes = pygame.transform.scale(pygame.image.load('pic/consignes.png'), (110, 80))
        self.commandes = pygame.image.load("pic/commandes.png")
    
    # Animation du fon
    def maj_bg(self):
        self.index += 1

        # Image de fond change a chaques tour
        if self.index >= len(self.menu_images):
            self.index = 0
        self.image = self.menu_images[self.index]
