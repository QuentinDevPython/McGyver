import pygame
from player import Player
from maze import Maze

# create a class that will represent the game


class Game:

    def __init__(self):
        self.player = Player()
        self.maze = Maze()
