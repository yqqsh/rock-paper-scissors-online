from typing import Optional

import pygame

UTIL_BAR_HEIGHT: int = 200
WIDTH: int = 512
HEIGHT: int = WIDTH + UTIL_BAR_HEIGHT
FPS: int

TITLE: str = "Shifty"
__MAIN_WIN: Optional[pygame.surface.Surface] = None


def get_main_surface(flags: int=0) -> pygame.surface.Surface:
    global __MAIN_WIN
    if __MAIN_WIN is None:
        __MAIN_WIN = pygame.display.set_mode((WIDTH, HEIGHT), flags)

    pygame.display.set_caption(TITLE)

    return __MAIN_WIN
