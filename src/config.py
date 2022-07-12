from typing import Optional

from pathlib import Path

import pygame


TILE_WIDTH: int = 64
TILE_HEIGHT: int = 64
TILE_SIZE: pygame.Vector2 = pygame.Vector2(TILE_WIDTH, TILE_HEIGHT)

UTIL_BAR_HEIGHT: int = 100

PADDING: pygame.Vector2 = pygame.Vector2(30, 20)

GRID_ROWS: int = 4
GRID_COLS: int = 5

WIDTH: int = TILE_WIDTH * GRID_ROWS
HEIGHT: int = UTIL_BAR_HEIGHT + TILE_HEIGHT * GRID_COLS
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


__all__ = [
    "TILE_WIDTH",
    "TILE_HEIGHT",
    "GRID_ROWS",
    "GRID_COLS",
    "TILE_SIZE",
    "UTIL_BAR_HEIGHT",
    "PADDING",
    "WIDTH",
    "HEIGHT",
    "SCREEN_SIZE",
    "FPS",
    "TITLE",
    "Paths",
    "get_main_surface",
]
