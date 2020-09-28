import pygame
from maze import Maze

# create a class that represent the player


class Player():

    def __init__(self):
        self.maze = Maze()
        self.maze.create_maze()
        self.velocity = 40
        self.player_image = pygame.image.load(
            'assets/characters/mac_gyver.png')
        self.player_image = pygame.transform.scale(self.player_image, (36, 38))
        self.rect = self.player_image.get_rect()
        self.rect.x = 40
        self.rect.y = 40

    def move_right(self):
        if self.maze.is_free_square(1, 0):
            self.rect.x += self.velocity
            self.maze.player_position = (
                self.maze.player_position[0] + 1, self.maze.player_position[1])

    def move_left(self):
        if self.maze.is_free_square(-1, 0):
            self.rect.x -= self.velocity
            self.maze.player_position = (
                self.maze.player_position[0] - 1, self.maze.player_position[1])

    def move_up(self):
        if self.maze.is_free_square(0, -1):
            self.rect.y -= self.velocity
            self.maze.player_position = (
                self.maze.player_position[0], self.maze.player_position[1] - 1)

    def move_down(self):
        if self.maze.is_free_square(0, 1):
            self.rect.y += self.velocity
            self.maze.player_position = (
                self.maze.player_position[0], self.maze.player_position[1] + 1)

    def is_victorious(self):
        if self.maze.is_guardian_square():
            print('Win')
            return True
        elif not self.maze.is_guardian_square():
            print('Defeat')
            pass
