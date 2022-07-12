from pathlib import Path

import pygame
import src.config as cfg
from src.game import Game


def main():
    game = Game(cfg.get_main_surface())

    pygame.display.set_icon(pygame.image.load(cfg.Paths.ASSETS / "Logo.png"))

    game.run()


main()
