import pygame
import src.config as cfg
from src.game import Game
import src.grid as grid


def main():
    game = Game(cfg.get_main_surface())

    grid.Blocks.load()

    pygame.display.set_icon(pygame.image.load(cfg.Paths.ASSETS / "Logo.png"))

    game.run()


main()
