from typing import Optional, Tuple, List

import src.config as cfg

import pygame


__instance: Optional["Mouse"] = None


class Mouse:
    def __init__(self) -> None:
        super().__init__()
        self.__x: int = 0
        self.__y: int = 0
        self.__prev_x: int = 0
        self.__prev_y: int = 0
        self.__pressed: Tuple[bool, bool, bool] = False, False, False
        self.__just_pressed: Tuple[bool, bool, bool] = False, False, False
        self.__just_released: Tuple[bool, bool, bool] = False, False, False

    @property
    def x(self) -> int:
        return self.__x

    @property
    def x_diff(self) -> int:
        return self.__x - self.__prev_x

    @property
    def y_diff(self) -> int:
        return self.__y - self.__prev_y

    @property
    def y(self) -> int:
        return self.__y

    @property
    def prev_x(self) -> int:
        return self.__prev_x

    @property
    def prev_y(self) -> int:
        return self.__prev_y

    @property
    def is_pressed(self) -> Tuple[bool, bool, bool]:
        return self.__pressed

    @property
    def is_left_pressed(self) -> bool:
        return self.__pressed[0]

    @property
    def is_middle_pressed(self) -> bool:
        return self.__pressed[1]

    @property
    def is_right_pressed(self) -> bool:
        return self.__pressed[2]

    @property
    def just_pressed(self) -> Tuple[bool, bool, bool]:
        return self.__just_pressed

    @property
    def just_pressed_left(self) -> bool:
        return self.__just_pressed[0]

    @property
    def just_pressed_middle(self) -> bool:
        return self.__just_pressed[1]

    @property
    def just_pressed_right(self) -> bool:
        return self.__just_pressed[2]

    @property
    def just_released(self) -> Tuple[bool, bool, bool]:
        return self.__just_released

    @property
    def just_released_left(self) -> bool:
        return self.__just_released[0]

    @property
    def just_released_middle(self) -> bool:
        return self.__just_released[1]

    @property
    def just_released_right(self) -> bool:
        return self.__just_released[2]

    def update(self, events: List[pygame.event.Event]) -> None:
        self.__pressed = (False, False, False)
        self.__just_pressed = (False, False, False)
        self.__just_released = (False, False, False)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.__pressed = True, self.__pressed[1], self.__pressed[2]
                    self.__just_pressed = True, self.__just_pressed[1], self.__just_pressed[2]
                elif event.button == 2:
                    self.__pressed = self.__pressed[0], True, self.__pressed[2]
                    self.__just_pressed = self.__just_pressed[0], True, self.__just_pressed[2]
                elif event.button == 3:
                    self.__pressed = self.__pressed[0], self.__pressed[1], True
                    self.__just_pressed = self.__just_pressed[0], self.__just_pressed[1], True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.__pressed = False, self.__pressed[1], self.__pressed[2]
                    self.__just_released = True, self.__just_released[1], self.__just_released[2]
                elif event.button == 2:
                    self.__pressed = self.__pressed[0], False, self.__pressed[2]
                    self.__just_released = self.__just_released[0], True, self.__just_released[2]
                elif event.button == 3:
                    self.__pressed = self.__pressed[0], self.__pressed[1], False
                    self.__just_released = self.__just_released[0], self.__just_released[1], True

        self.__prev_x = self.__x
        self.__prev_y = self.__y
        self.__x, self.__y = pygame.mouse.get_pos()

    @staticmethod
    def create():
        global __instance
        if __instance is None:
            __instance = Mouse()
        return __instance
