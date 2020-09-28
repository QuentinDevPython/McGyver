import pygame
from player import Player
from maze import Maze
from items import Items

'''class that will represent the game'''


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

    '''function to check a collision between a sprite and a group of sprites'''

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    '''function to determine if an item was removed from the group of items (so removed from the maze) or not'''

    def is_in_all_items(self, item):
        for sprite in self.all_items:
            if item == sprite:
                return True

    '''function to spawn the items in the maze at the beginning of the game'''

    def spawn_items(self):
        self.all_items.add(self.item_needle)
        self.all_items.add(self.item_tube)
        self.all_items.add(self.item_ether)
        self.all_items.add(self.item_syringe)
