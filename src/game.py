import pygame
import math
import sys
import os


class Game:
    def __init__(self, WIN: pygame.surface.Surface):
        self.SCREEN_SIZE: pygame.Vector2 = pygame.Vector2(WIN.get_size())
        self.W: int = self.SCREEN_SIZE.x
        self.H: int = self.SCREEN_SIZE.y
        self.WIN: pygame.surface.Surface = WIN

        self.running: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()

    def update(self) -> None:
        pass

    def event_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def draw(self) -> None:
        self.WIN.fill((30, 30, 30))
        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.clock.tick()
            self.event_handler()
            self.update()
            self.draw()
