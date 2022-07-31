from typing import Dict

import numpy as np

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


class Solution:
    _grid: np.ndarray
    background: pygame.Surface

    def __init__(self) -> None: ...

    def random_gen(self) -> None: ...
    def draw_to(self, surface: pygame.Surface) -> None: ...
    def draw(self) -> None: ...