from typing import Optional

from pygame._common import ColorValue, Coordinate
import pygame


class Button:
    x: int
    y: int
    w: int
    h: int
    rect: pygame.Rect
    image: Optional[pygame.Surface]

    def __init__(self, text: str, x: int, y: int, w: int, h: int) -> None: ...
    def draw(self, color: ColorValue) -> None: ...
    def draw_to(self, surface: pygame.Surface, color: ColorValue) -> None: ...
    def is_over(self, pos: Coordinate) -> bool: ...
    def is_clicked(self, event: pygame.event.Event) -> bool: ...
