import pygame

class Book(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.vitesse = 12
        self.image = pygame.image.load("pic/book.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.player = player

    def delete(self):
        self.player.group_projectiles.remove(self)

    def move(self):
        # Si le joueur est le joueur 1
        
        if not self.player.is_bot :
            # Vérification des collisions avec le bot ou joueur 2
            if self.player.p == 1:
                if pygame.sprite.spritecollide(self.player.game.bot, self.player.group_projectiles, False, pygame.sprite.collide_mask) :
                    self.delete()
                    self.player.game.bot.vie -= 10
                
                # Si livre sort de l'ecran
                elif self.rect.x > 1580:
                    self.delete()
                
                # Sinon continu d'avancer
                else:
                    self.rect.x += self.vitesse
            
            # Si bot est un joueur, vérification collisions avec joueur 1
            if self.player.p == 2:
                if pygame.sprite.spritecollide(self.player.game.player1, self.player.group_projectiles, False, pygame.sprite.collide_mask):
                    self.delete()
                    self.player.game.player1.vie -= 10
                    
                elif self.rect.x < -200:
                    self.delete()

                else:
                    self.rect.x -= self.vitesse

        # Si le joueur est un robot ou le joueur 2
        elif self.player.is_bot:
            
            # Vérification des collisions avec le joueur 1
            if pygame.sprite.spritecollide(self.player.game.player1, self.player.group_projectiles, False, pygame.sprite.collide_mask):
                self.delete()
                self.player.game.player1.vie -= 10
            
            else:
                self.rect.x -= self.vitesse
        
        elif self.rect.x > 1280 or self.rect.x < 0:
            self.delete()
        