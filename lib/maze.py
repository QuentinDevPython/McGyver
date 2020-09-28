import pygame
import random


class Maze:

    def __init__(self):
        self.wall = []
        self.floor = []
        self.start = []
        self.end = []
        self.wall_image = pygame.image.load('assets/background/wall.png')
        self.wall_image = pygame.transform.scale(self.wall_image, (40, 40))
        self.floor_image = pygame.image.load('assets/background/floor.png')
        self.floor_image = pygame.transform.scale(self.floor_image, (40, 40))
        self.start_image = pygame.image.load('assets/background/start.png')
        self.start_image = pygame.transform.scale(self.start_image, (40, 40))
        self.end_image = pygame.image.load('assets/background/end.png')
        self.end_image = pygame.transform.scale(self.end_image, (40, 40))
        self.guardian_image = pygame.image.load(
            'assets/characters/guardian.png')
        self.player_position = (1, 1)
        self.item_position = (0, 0)

    def create_maze(self):

        maze = []

        index = 0
        WIDTH = 15
        LENGHT = 15

        for line_maze in range(LENGHT):
            maze.append([0] * WIDTH)

        maze_file = open("lib/maze_grid.txt", "r")
        contenu_maze_file = maze_file.read()
        contenu_maze_file = contenu_maze_file.split()

        for column_maze in range(WIDTH):
            for line_maze in range(LENGHT):
                if (column_maze, line_maze) != (0, 0):
                    index += 1
                maze[column_maze][line_maze] = contenu_maze_file[index]

        maze_file.close()

        for line_maze in range(15):
            for column_maze in range(15):
                if maze[line_maze][column_maze] == '9':
                    self.wall.append((column_maze, line_maze))
                if maze[line_maze][column_maze] == '0':
                    self.floor.append((column_maze, line_maze))
                if maze[line_maze][column_maze] == '1':
                    self.start.append((column_maze, line_maze))
                if maze[line_maze][column_maze] == '2':
                    self.end.append((column_maze, line_maze))

    def create_maze_map(self, screen):

        for wall in self.wall:
            screen.blit(self.wall_image, (wall[0] * 40, wall[1] * 40))
        for floor in self.floor:
            screen.blit(self.floor_image, (floor[0] * 40, floor[1] * 40))
        for start in self.start:
            screen.blit(self.start_image, (start[0] * 40, start[1] * 40))
        for end in self.end:
            screen.blit(self.end_image, (end[0] * 40, end[1] * 40))
            screen.blit(self.guardian_image,
                        (end[0] * 40 + 3, end[1] * 40 + 2))

    def is_free_square(self, x, y):
        can_move_right = False
        next_player_position = (
            self.player_position[0] + x, self.player_position[1] + y)
        for floor in self.floor:
            if next_player_position == floor:
                can_move_right = True
        for start in self.start:
            if next_player_position == start:
                can_move_right = True
        return can_move_right

    def is_guardian_square(self):
        next_player_position = (
            self.player_position[0] + 1, self.player_position[1])
        for end in self.end:
            if next_player_position == end:
                return True

    @property
    def is_item_square(self):
        position = False
        while position == False:
            self.item_position = (random.randint(1, 15), random.randint(1, 15))
            for floor in self.floor:
                if self.item_position == floor:
                    position = True
                    return self.item_position
                else:
                    position = False
