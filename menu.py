import pygame

class Menu():
    def __init__(self):
        self.menu_images = []
        for x in range(1, 128):
            self.menu_images.append(pygame.transform.scale(pygame.image.load("pic/menu/f ({}).gif".format(str(x))), (1280,720)))
        self.image = self.menu_images[0]
        self.index = 0
        self.button_bot = pygame.image.load("pic/button_bot.png")
        self.button_pvp = pygame.image.load("pic/button_pvp.png")
        self.title = pygame.image.load("pic/title.png")
    
    
    def maj_bg(self):
        self.index += 1
        if self.index >= len(self.menu_images):
            self.index = 0
        self.image = self.menu_images[self.index]
