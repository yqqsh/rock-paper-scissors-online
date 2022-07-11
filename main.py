import pygame
import src.config as config
from src.game import Game


def main():
    game = Game(config.get_main_surface())
    game.run()


main()
