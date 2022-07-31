from typing import Optional, Tuple, Callable, List, Union, Dict


import src.config as cfg
import src.utils as utils
import src.grid as grid

import numpy as np

import pygame
import random


class Blocks:
    BLOCK_NONE: int = grid.Blocks.BLOCK_NONE
    BLOCK_1x1: int = grid.Blocks.BLOCK_1x1
    BLOCK_2x1: int = grid.Blocks.BLOCK_2x1
    BLOCK_1x2: int = grid.Blocks.BLOCK_1x2
    BLOCK_2x2: int = grid.Blocks.BLOCK_2x2

    CODE: Dict[int, pygame.Surface] = {}

    @classmethod
    def load(cls) -> None:
        cls.CODE[cls.BLOCK_1x1] = utils.load_image(cfg.Paths.ASSETS / "1x1sqSolDis.png")
        cls.CODE[cls.BLOCK_2x1] = pygame.image.load(cfg.Paths.ASSETS / "2x1sqSolDis.png")
        cls.CODE[cls.BLOCK_1x2] = pygame.image.load(cfg.Paths.ASSETS / "1x2sqSolDis.png")
        cls.CODE[cls.BLOCK_2x2] = pygame.image.load(cfg.Paths.ASSETS / "2x2sqSolDis.png")


class Solution:
    def __init__(self) -> None:
        self._grid: grid.Grid = grid.Grid()
        self.background: pygame.Surface = pygame.image.load(cfg.Paths.ASSETS / "solutiondisplay.png")

        Blocks.load()

    def random_gen(self) -> None:
        for row in range(cfg.GRID_ROWS):
            for col in range(cfg.GRID_COLS):
                self._grid.set_at(row, col, random.randint(0, 4))

    def draw_to(self, surface: pygame.Surface) -> None:
        sol_x: int = 20
        sol_y: int = (int(cfg.UTIL_BAR_HEIGHT // 2)) - int(self.background.get_height() // 2)

        surface.blit(self.background, (sol_x, sol_y))

        for rowi, row in enumerate(self._grid.get_grid()):
            for coli, value in enumerate(row):
                if value == 0:
                    continue

                x = (sol_x + 1 + coli) + coli * cfg.SOL_TILE_SIZE.x
                y = (sol_y + 1 + rowi) + rowi * cfg.SOL_TILE_SIZE.y
                surface.blit(Blocks.CODE[value], (x, y))

    def draw(self) -> None:
        self.draw_to(cfg.get_main_surface())
