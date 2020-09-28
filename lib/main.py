import pygame
from game import Game

pygame.init()

# define the dimensions of the game window
number_squares = 15
size_squares = 40
screen_size = (number_squares * size_squares, number_squares * size_squares)

# generate the game window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Escape from the maze')

# load the game
game = Game()

# create the maze
game.maze.create_maze()

running = True

while running:

    game.maze.create_maze_map(screen)

    game.all_items.draw(screen)
    screen.blit(game.player.image, game.player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.player.is_collision()
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
                if game.player.is_victorious():
                    running = False
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
            elif event.key == pygame.K_UP:
                game.player.move_up()
            elif event.key == pygame.K_DOWN:
                game.player.move_down()
