from typing import Optional, Dict, Tuple

from pathlib import Path

import pygame


TILE_WIDTH: int = 64
TILE_HEIGHT: int = 64
TILE_SIZE: pygame.Vector2 = pygame.Vector2(TILE_WIDTH, TILE_HEIGHT)

SOL_TILE_WIDTH: int = 12
SOL_TILE_HEIGHT: int = 12
SOL_TILE_SIZE: pygame.Vector2 = pygame.Vector2(SOL_TILE_WIDTH, SOL_TILE_HEIGHT)

RESET_WIDTH: int = 40
RESET_HEIGHT: int = 40

UTIL_BAR_HEIGHT: int = 100

GRID_ROWS: int = 5
GRID_COLS: int = 4

PADDING: pygame.Vector2 = pygame.Vector2(GRID_COLS + 1, GRID_ROWS + 1)

WIDTH: int = TILE_WIDTH * GRID_COLS + PADDING.x
HEIGHT: int = UTIL_BAR_HEIGHT + TILE_HEIGHT * GRID_ROWS + PADDING.y
SCREEN_SIZE: pygame.Vector2 = pygame.Vector2(WIDTH, HEIGHT)

FPS: int = 60

TITLE: str = "Shifty"
__MAIN_WIN: Optional[pygame.surface.Surface] = None


# meant to be used as a namespace
class Paths:
    DATA: Path = Path(__file__).parent.parent.joinpath("data")
    ANIMATIONS: Path = DATA.joinpath("animations")
    ASSETS: Path = DATA.joinpath("assets")
    SOUNDS: Path = DATA.joinpath("sounds")
    SOUNDTRACKS: Path = DATA.joinpath("soundtracks")
    FONTS: Path = DATA.joinpath("fonts")


def get_main_surface(flags: int=0) -> pygame.surface.Surface:
    global __MAIN_WIN
    if __MAIN_WIN is None:
        __MAIN_WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags)

    pygame.display.set_caption(TITLE)

    return __MAIN_WIN


__cached_fonts: Dict[Tuple[Optional[str], int], pygame.font.Font] = {}


def get_font(path: Optional[str]=None, size: int=50) -> pygame.font.Font:
    key = (path, size)
    if key not in __cached_fonts:
        __cached_fonts[key] = pygame.font.Font(path, size)

    return __cached_fonts[key]


__all__ = [
    "TILE_WIDTH",
    "TILE_HEIGHT",
    "TILE_SIZE",
    "SOL_TILE_WIDTH",
    "SOL_TILE_HEIGHT",
    "SOL_TILE_SIZE",
    "RESET_WIDTH",
    "RESET_HEIGHT",
    "UTIL_BAR_HEIGHT",
    "GRID_ROWS",
    "GRID_COLS",
    "PADDING",
    "WIDTH",
    "HEIGHT",
    "SCREEN_SIZE",
    "FPS",
    "TITLE",
    "Paths",
    "get_main_surface",
    "get_font",
]
