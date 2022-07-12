"""
a grid class

lets say 1 is 2x2

this is valid cause the topleft of the 2x2 block is in 3-2 position
[[0, 0, 0, 0]
 [0, 0, 0, 0]
 [0, 0, 0, 0]
 [0, 0, 1, 0]
 [0, 0, 0, 0]]

but this is not valid as it says there are four 2x2 blocks
[[0, 0, 0, 0]
 [0, 0, 0, 0]
 [0, 0, 0, 0]
 [0, 0, 1, 1]
 [0, 0, 1, 1]]
"""


from typing import List, Dict, Tuple, Optional

import src.config as cfg
import src.utils as utils

import pygame
import math
import sys
import os


class Blocks:
    BLOCK_NONE: int = 0
    BLOCK_1x1: int = 1
    BLOCK_2x1: int = BLOCK_1x1 + 1
    BLOCK_1x2: int = BLOCK_2x1 + 1
    BLOCK_2x2: int = BLOCK_1x2 + 1

    CODE: Dict[int, pygame.Surface] = {}

    @classmethod
    def load(cls) -> None:
        cls.CODE[cls.BLOCK_1x1] = utils.load_image(cfg.Paths.ASSETS / "1x1sq.png")
        cls.CODE[cls.BLOCK_2x1] = pygame.image.load(cfg.Paths.ASSETS / "2x1sq.png")
        cls.CODE[cls.BLOCK_1x2] = pygame.image.load(cfg.Paths.ASSETS / "1x2sq.png")
        cls.CODE[cls.BLOCK_2x2] = pygame.image.load(cfg.Paths.ASSETS / "2x2sq.png")


class Grid:
    def __init__(self) -> None:
        self.rows: int = cfg.GRID_ROWS
        self.cols: int = cfg.GRID_COLS

        self.cell_size: int = cfg.TILE_SIZE.x

        self._grid: List[List[int]] = [[0 for _ in range(self.rows)] for _ in range(self.cols)]

        self.grid_surface: pygame.Surface = utils.load_image(cfg.Paths.ASSETS / "playinggrid.png")

    def print(self) -> None:
        print("[" + "\n ".join(str(row) for row in self._grid) + "]")

    def draw_to(self, surface: pygame.surface.Surface) -> None:
        surface.blit(self.grid_surface, (0, cfg.UTIL_BAR_HEIGHT))

        for rowi, row in enumerate(self._grid):
            for coli, value in enumerate(row):
                if value == 0:
                    continue
                x = 1 + coli + coli * self.cell_size
                y = 1 + rowi + rowi * self.cell_size + cfg.UTIL_BAR_HEIGHT
                surface.blit(Blocks.CODE[value], (x, y))

    def draw(self) -> None:
        self.draw_to(cfg.get_main_surface())
