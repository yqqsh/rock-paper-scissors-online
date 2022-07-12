from typing import Dict, List

import pygame


class Blocks:
    BLOCK_NONE: int
    BLOCK_1x1: int
    BLOCK_2x1: int
    BLOCK_1x2: int
    BLOCK_2x2: int

    CODE: Dict[int, pygame.Surface]

    @classmethod
    def load(cls) -> None: ...


class Grid:
    rows: int
    cols: int
    cell_size: int
    _grid: List[List[int]]
    grid_surface: pygame.Surface
    def __init__(self) -> None: ...
    def draw_to(self, surface: pygame.Surface) -> None: ...
    def draw(self) -> None: ...
    def print(self) -> None: ...
