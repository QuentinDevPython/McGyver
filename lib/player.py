import pygame
from maze import Maze

'''class that represents the player'''


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        self.game = game
        super().__init__()
        self.maze = Maze()
        self.maze.create_maze()
        self.velocity = 40
        self.image = pygame.image.load(
            'assets/characters/mac_gyver.png')
        self.image = pygame.transform.scale(self.image, (36, 38))
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 40
        self.inventory = []

    '''function to determine if the player have a collision with an item, if it is the case the player collect the item in his inventory,
    the item is removed from the maze'''

    def is_collision(self):
        position_player = (self.rect.x, self.rect.y)
        if self.game.check_collision(self, self.game.all_items):
            self.inventory.append('True')
            if position_player == self.game.item_needle.item_position and self.game.is_in_all_items(self.game.item_needle):
                self.game.all_items.remove(self.game.item_needle)
            elif position_player == self.game.item_tube.item_position and self.game.is_in_all_items(self.game.item_tube):
                self.game.all_items.remove(self.game.item_tube)
            elif position_player == self.game.item_syringe.item_position and self.game.is_in_all_items(self.game.item_syringe):
                self.game.all_items.remove(self.game.item_syringe)
            elif position_player == self.game.item_ether.item_position and self.game.is_in_all_items(self.game.item_ether):
                self.game.all_items.remove(self.game.item_ether)

    '''function to move the player ans its image at his right and retrieve its position from the maze grid'''

    def move_right(self):
        if self.maze.is_free_square(1, 0):
            self.rect.x += self.velocity
            self.maze.player_position = (
                self.maze.player_position[0] + 1, self.maze.player_position[1])

    '''function to move the player ans its image at his left and retrieve its position from the maze grid'''

    def move_left(self):

        if self.maze.is_free_square(-1, 0):
            self.rect.x -= self.velocity
            self.maze.player_position = (
                self.maze.player_position[0] - 1, self.maze.player_position[1])

    '''function to move the player ans its image up and retrieve its position from the maze grid'''

    def move_up(self):

        if self.maze.is_free_square(0, -1):
            self.rect.y -= self.velocity
            self.maze.player_position = (
                self.maze.player_position[0], self.maze.player_position[1] - 1)

    '''function to move the player ans its image down and retrieve its position from the maze grid'''

    def move_down(self):

        if self.maze.is_free_square(0, 1):
            self.rect.y += self.velocity
            self.maze.player_position = (
                self.maze.player_position[0], self.maze.player_position[1] + 1)

    '''function to determine if the player have won or is defeat when he arrives next to the arrival square, and quits the game printing "Win" or "Defeat" '''

    def is_victorious(self):
        if self.maze.is_guardian_square() and self.inventory == ['True', 'True', 'True', 'True']:
            print('Win')
            pygame.quit()
            return True
        elif self.maze.is_guardian_square():
            print('Defeat')
            pygame.quit()
            return True
