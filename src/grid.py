from typing import List

import src.config as cfg

import pygame
import math
import sys
import os


class Grid:
    def __init__(self) -> None:
        self.rows: int = cfg.GRID_ROWS
        self.cols: int = cfg.GRID_COLS

        self.cell_size: int = cfg.TILE_SIZE.x

        self._grid: List[List[int]] = [[0 for _ in range(self.rows)] for _ in range(self.cols)]

    def print(self) -> None:
        print("[" + "\n ".join(str(row) for row in self._grid) + "]")
