import pygame

# create a class that represent the player


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.velocity = 40
        self.image = pygame.image.load('assets/characters/mac_gyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
