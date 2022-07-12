from typing import Tuple, Union, List

from pathlib import Path

import pygame

def load_image(path: Union[Path, str]) -> pygame.surface.Surface: ...
def load_alpha_image(path: Union[Path, str]) -> pygame.surface.Surface: ...
def resize_smooth_image(image: pygame.Surface, new_size: Tuple[int, int]) -> pygame.surface.Surface: ...
def resize_image(image: pygame.Surface, new_size: Tuple[int, int]) -> pygame.surface.Surface: ...
def resize_image_ratio(image: pygame.Surface, new_size: Tuple[int, int]) -> pygame.surface.Surface: ...
def resize_by_x(image: pygame.surface.Surface, amount: Union[int, float]) -> pygame.surface.Surface: ...
def get_font(size, type_of_font="comicsans") -> pygame.font.Font: ...
def wrap_multi_lines(
        text: str,
        font: pygame.font.Font,
        max_width: int,
        max_height: int=0,
        antialias: bool=True
) -> List[str]: ...
def blit_multiple_lines(
        x: int,
        y: int,
        lines: list,
        WIN: pygame.surface.Surface,
        font: pygame.font.Font,
        centered_x=False,
        centered_x_pos: int=None,
        color: Tuple[int, int, int]=(0, 0, 0)
) -> None: ...
def pixel_perfect_collision(
        image_1: pygame.surface.Surface, image_1_pos:
        Tuple[int, int], image_2:
        pygame.surface.Surface,
        image_2_pos: Tuple[int, int]
) -> bool: ...
