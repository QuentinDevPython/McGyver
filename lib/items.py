import pygame
from player import Player

'''class that manages the items that the player must collect'''


class Items(pygame.sprite.Sprite):

    def __init__(self, image_name, game):
        super().__init__()
        self.player = Player(game)
        self.image = pygame.image.load('assets/items/' + image_name)
        self.rect = self.image.get_rect()
        self.item_position = self.position
        self.rect.x = self.item_position[0]
        self.rect.y = self.item_position[1]

    '''function to delete an item when it is taken by the player'''

    def remove(self):
        self.player.game.all_items.remove(self)

    '''property which retrieves the coordinates of an item in the grid and positions it correctly to be displayed'''
    @property
    def position(self):
        item_position = self.player.maze.is_item_square

        item_position = (
            item_position[0] * 40, item_position[1] * 40)

        return item_position
