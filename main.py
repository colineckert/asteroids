import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(screen.get_width() / 2, screen.get_height() / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
