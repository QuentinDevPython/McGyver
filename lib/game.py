import pygame
from player import Player
from maze import Maze
from items import Items

# create a class that will represent the game


class Game:

    def __init__(self):
        self.all_items = pygame.sprite.Group()
        self.player = Player(self)
        self.maze = Maze()
        self.item_needle = Items('needle.png', self)
        self.item_tube = Items('plastic_tube.png', self)
        self.item_ether = Items('ether.png', self)
        self.item_syringe = Items('syringe.png', self)
        self.spawn_items()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_items(self):
        self.all_items.add(self.item_needle)
        self.all_items.add(self.item_tube)
        self.all_items.add(self.item_ether)
        self.all_items.add(self.item_syringe)
