from joueur import Player
import pygame

class Game():
    def __init__(self):
        self.player1 = Player(100, 10, 20, 6, "ch", False, self)
        self.bot = Player(100, 10, 20, 6, "ci", True, self)
        self.pressed = {}
        self.is_playing = False
        self.image = pygame.image.load("pic/street/street1.png")
        self.finish1 = pygame.transform.scale(pygame.image.load("pic/won1.png"), (500, 100))
        self.finish2 = pygame.transform.scale(pygame.image.load("pic/loose1.png"), (500, 100))
        self.orientation = True
    def gravity(self):
        if self.player1.rect.y < 400:
            self.player1.rect.y += 10
        if self.bot.rect.y < 400:
            self.bot.rect.y += 10


    def start(self,root_page):
        
        # Verification de la vie des persos
        if self.bot.vie <= 0:
            root_page.blit(self.finish2, (350,260))
        elif self.player1.vie <= 0:
            root_page.blit(self.finish1, (350,260))
        else:
            # Mise en place du perso en fonction de son orientation par rapport a l'autre
            root_page.blit(self.player1.image, self.player1.rect)
            root_page.blit(self.bot.image, self.bot.rect)

            # Affichage des projectiles (le groupe)
            self.player1.group_projectiles.draw(root_page)
            self.bot.group_projectiles.draw(root_page)
            
            self.bot.decision()
            #image fix quand le personnage est a l'arrêt
            if not self.pressed.get(pygame.K_RIGHT) and not self.pressed.get((pygame.K_LEFT)) and self.player1.on_ground():
                if self.orientation:
                    self.player1.image = self.player1.images[1]
                else:
                    self.player1.image = self.player1.images2[1]
            
            if not self.player1.on_ground():
                if self.orientation:
                    self.player1.image = self.player1.images[2]
                else:
                    self.player1.image = self.player1.images2[2]


            #action fluide grace au dictionnaire "pressed"
            if self.pressed.get(pygame.K_RIGHT) :
                self.player1.avancer()

            # elif self.pressed.get(pygame.K_RIGHT) and self.player1.on_ground():
            #     self.player1.avancer()                         #Pour faire des saut avec les jambe qui ne bouge pas en l'air
            #     self.player1.image = self.player1.images[2]
            

            if self.pressed.get(pygame.K_LEFT) :
                self.player1.reculer()

            # elif self.pressed.get(pygame.K_LEFT) and self.player1.on_ground():
            #     self.player1.reculer()                         #Pour faire des saut avec les jambe qui ne bouge pas en l'air
            #     self.player1.image = self.player1.images[2]
            
            
            #application de la grvité et du saut

            #peut-etre rajouter deuxieme palier pour eviter de voler
            if self.pressed.get(pygame.K_UP):
                self.player1.sauter()
            
            if self.pressed.get(pygame.K_DOWN) and not self.pressed.get(pygame.K_LEFT) and not self.pressed.get(pygame.K_RIGHT) and self.player1.on_ground():
                self.player1.baisser()
            self.gravity()
