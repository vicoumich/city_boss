import pygame
from random import randint
from book import Book

class Player(pygame.sprite.Sprite):
    def __init__(self, vie, degats, spe, vitesse, name, is_bot, game):
        super().__init__()
        self.is_bot = is_bot
        self.vie = vie
        self.max_vie = vie
        self.degats = degats
        self.spe = spe
        self.vitesse = vitesse
        self.group_projectiles = pygame.sprite.Group()
        self.game = game
        
        # Animation déplacement
        self.images = []
        self.image = pygame.image.load("pic/{}1.png".format(name))
        self.images.append(self.image)
        self.images.append(pygame.image.load("pic/{}2.png".format(name)))
        self.images.append(pygame.image.load("pic/{}3.png".format(name)))
        self.index = 0

        # Animation quand le perso se retourne
        self.images2 = []
        self.image2 = pygame.transform.flip(self.image, True, False)
        for image in self.images:
            self.images2.append(pygame.transform.flip(image, True, False))

        # Animation accroupi
        self.accroupi = pygame.image.load('pic/{}4.png'.format(name))
        
        self.rect = self.image.get_rect()
        if self.is_bot:
            self.rect.x = 1000
        else:
            self.rect.x = 20
        self.rect.y = 0
        self.touch = False
        self.count = 0
        self.state = 0
    
    def avancer(self):
        if self.rect.x < 1280 - 200:
            self.rect.x += self.vitesse
            self._maj_deplacement()
    
    def reculer(self):
        if self.rect.x > -50:   
            self.rect.x -= self.vitesse
            self._maj_deplacement()

    def _maj_deplacement(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
    
    def on_ground(self):
        return self.rect.y == 401 or self.rect.y == 400 

    def sauter(self):
        if self.rect.y > 200 and not self.touch:
            self.rect.y -= 8
            
            if self.rect.y < 200:
                self.touch = True
        if self.on_ground():
            self.touch = False

    def baisser(self):
        self.image = self.accroupi
        a = self.rect.x
        b = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = a
        self.rect.y = b

    def attaque(self):
        self.group_projectiles.add(Book(self))



#########################
# Méthode pour le robot #
#########################
    def action(self):
        if self.state == 1:
            self.reculer()
        elif self.state == 2:
            self.avancer()
        elif self.state == 3:
            self.sauter()
        elif self.state == 4:
            self.baisser()


    def decision(self):
        # Mode offensif si il a plus 30PV
        if self.vie > 30 and self.rect.x > 940:
            #Prise de décisions
            # Continuer de sauter quand il est en l'air
            if not self.touch and not self.on_ground():
                self.state = 3
            else:
                a = randint(0, 100)
                if a == 0 or a == 1 or a == 3 or a == 4 or a == 5 or a == 7:
                    self.state = 1
                elif a == 2:
                    self.state = 2
                elif a == 6:
                    self.state = 3
                elif a == 8:
                    self.state = 4
                elif a == 9 or a == 10 or a == 11 or a == 12 or a == 13 or a == 14:
                    self.state == 5
        
        
        # Mode défensif si il a moins de 30PV
        else:
            # Prise de décisions
            # Continuer de sauter quand il est en l'air
            if not self.touch and not self.on_ground():
                self.state = 3
            else:
                a = randint(0, 100)
                if a == 0 or a == 10 or a == 11:
                    self.state = 1
                elif a == 1 or a == 2 or a == 9 :
                    self.state = 2
                elif a == 3 or a == 4:
                    self.state = 3
                elif a == 12: 
                    self.state = 4
                elif a == 13:
                    self.state = 5
        
        self.action()    
        