import src.config as config

import src.colors as colors
import src.grid as grid

import pygame
import math
import sys
import os


class Game:
    def __init__(self, WIN: pygame.surface.Surface):
        # display related attributes
        self.SCREEN_SIZE: pygame.Vector2 = pygame.Vector2(WIN.get_size())
        self.W: int = self.SCREEN_SIZE.x
        self.H: int = self.SCREEN_SIZE.y
        self.WIN: pygame.surface.Surface = WIN

        # clock related attributes
        self.running: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()

        # game objects
        self.grid: grid.Grid = grid.Grid()

    def update(self) -> None:
        pass

    def event_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def draw(self) -> None:
        self.WIN.fill((30, 30, 30))

        pygame.draw.rect(self.WIN, colors.black, pygame.Rect(0, 0, config.WIDTH, config.UTIL_BAR_HEIGHT))

        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.clock.tick(config.FPS)
            self.event_handler()
            self.update()
            self.draw()
