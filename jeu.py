from joueur import Player
import pygame

class Game():
    def __init__(self):
        # Creation des joueurs
        self.player1 = Player(100, 10, 20, 6, "ch", False, self, 1)
        self.bot = Player(100, 10, 20, 6, "ci", True, self, 2)

        #dictionnaire des touches appuyées en direct
        self.pressed = {}

        self.is_playing = False

        self.image = pygame.image.load("pic/street/street1.png")
        self.finish1 = pygame.transform.scale(pygame.image.load("pic/won1.png"), (500, 100))
        self.finish2 = pygame.transform.scale(pygame.image.load("pic/loose1.png"), (500, 100))
        self.orientation = True
    
    def gravity(self):
        if self.player1.rect.y < 400:
            self.player1.rect.y += 10  # Ramene les joueurs vers le sol en permennance
        if self.bot.rect.y < 400:
            self.bot.rect.y += 10

    def start_pvp(self, root_page):
        # Le bot devient joueur 2
        self.bot.is_bot = False
        self.bot.p = 2
        
        # Vérification de la vie des persos
        if self.bot.vie <= 0:
            root_page.blit(self.finish2, (350,260))
        elif self.player1.vie <= 0:
            root_page.blit(self.finish1, (350,260))
        else:
            root_page.blit(self.player1.image, self.player1.rect)
            root_page.blit(self.bot.image, self.bot.rect)

            # Affichage des projectiles (le groupe des projectiles)
            self.player1.group_projectiles.draw(root_page)
            self.bot.group_projectiles.draw(root_page)
            
            #image fix du joueur 1
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

            # Images fix du joueur 2
            if not self.pressed.get(pygame.K_d) and not self.pressed.get((pygame.K_a)) and self.bot.on_ground():
                if self.orientation:
                    self.bot.image = self.bot.images[1]
                else:
                    self.bot.image = self.bot.images2[1]
            
            if not self.bot.on_ground():
                if self.orientation:
                    self.bot.image = self.bot.images[2]
                else:
                    self.bot.image = self.bot.images2[2]


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
            
            
           

            #peut-etre rajouter deuxieme palier pour eviter de voler
            if self.pressed.get(pygame.K_UP):
                self.player1.sauter()
            
            if self.pressed.get(pygame.K_w):
                self.bot.sauter()

            # Déplacement verticale du joueur2
            if self.pressed.get(pygame.K_s) and not self.pressed.get(pygame.K_a) and not self.pressed.get(pygame.K_d) and self.player1.on_ground():
                self.bot.baisser()

            if self.pressed.get(pygame.K_DOWN) and not self.pressed.get(pygame.K_LEFT) and not self.pressed.get(pygame.K_RIGHT) and self.player1.on_ground():
                self.player1.baisser()
            
            # Déplacement latérale du joueur2
            if self.pressed.get(pygame.K_a):
                self.bot.reculer()

            if self.pressed.get(pygame.K_d) :
                self.bot.avancer()
            
            #application de la grvité
            self.gravity()


    def start(self,root_page):
        
        # Verification de la vie des persos
        if self.bot.vie <= 0:
            root_page.blit(self.finish2, (350,260))
        elif self.player1.vie <= 0:
            root_page.blit(self.finish1, (350,260))
        else:
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
