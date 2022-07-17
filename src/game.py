from typing import List, Tuple, Union, Optional

import src.config as cfg

import src.colors as colors
import src.grid as grid
import src.mouse as mouse

import numpy as np

import pygame
import math
import sys
import os


class Game:
    def __init__(self, WIN: pygame.surface.Surface):
        # display related attributes
        self.SCREEN_SIZE: pygame.Vector2 = pygame.Vector2(WIN.get_size())
        self.W: int = self.SCREEN_SIZE.x
        self.H: int = self.SCREEN_SIZE.y
        self.WIN: pygame.surface.Surface = WIN

        # clock related attributes
        self.running: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.click_pos: Optional[pygame.Vector2] = None
        self.grid_pos: Optional[grid.GridVector] = None
        self.true_block_pos: Optional[grid.GridVector] = None

        # game objects
        self.mouse: mouse.Mouse = mouse.Mouse()
        self.grid: grid.Grid = grid.Grid()

        self.grid.set([[4, 0, 0, 0],
                       [0, 0, 1, 0],
                       [2, 0, 0, 0],
                       [3, 3, 1, 1],
                       [0, 0, 0, 0]])

    def update(self) -> None:
        pass

    def event_handler(self) -> None:
        events = pygame.event.get()

        self.mouse.update(events)

        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        if self.mouse.just_pressed_left:
            if self.mouse.y > cfg.UTIL_BAR_HEIGHT:
                col = int(self.mouse.x // cfg.TILE_SIZE.x)
                row = int((self.mouse.y - cfg.UTIL_BAR_HEIGHT) // cfg.TILE_SIZE.y)

                if not self.grid.if_block_at(row, col):
                    return

                cell = self.grid.block_at(row, col)
                self.true_block_pos = self.grid.locate_block(row, col, cell)

                self.click_pos = pygame.Vector2(self.mouse.x, self.mouse.y)
                self.grid_pos = grid.GridVector.from_mouse(self.mouse)

                print(f"valid click! grid_pos={self.grid_pos} {cell=}")

        if self.mouse.just_released_left:
            if self.click_pos is not None:
                self.click_pos = None
                self.grid_pos = None
                self.true_block_pos = None

        if self.grid_pos is not None:
            new_grid_pos = grid.GridVector.from_mouse(self.mouse)

            if self.grid_pos == new_grid_pos:
                return

            if self.grid_pos.col < new_grid_pos.col < cfg.GRID_COLS:
                print("move_right")
                if self.grid.move_right(self.true_block_pos.row, self.true_block_pos.col):
                    self.true_block_pos.col += 1
            elif -1 < new_grid_pos.col < self.grid_pos.col:
                print("move_left")
                if self.grid.move_left(self.true_block_pos.row, self.true_block_pos.col):
                    self.true_block_pos.col -= 1

            if self.grid_pos.row < new_grid_pos.row < cfg.GRID_ROWS:
                print("move_down")
                if self.grid.move_down(self.true_block_pos.row, self.true_block_pos.col):
                    self.true_block_pos.row += 1
            elif -1 < new_grid_pos.row < self.grid_pos.row:
                print("move_up")
                if self.grid.move_up(self.true_block_pos.row, self.true_block_pos.col):
                    self.true_block_pos.row -= 1

            self.grid_pos = new_grid_pos

    def draw(self) -> None:
        self.WIN.fill((30, 30, 30))

        pygame.draw.rect(self.WIN, colors.black, pygame.Rect(0, 0, cfg.WIDTH, cfg.UTIL_BAR_HEIGHT))

        self.grid.draw_to(self.WIN)

        pygame.display.update()

    def run(self) -> None:
        while self.running:
            self.clock.tick(cfg.FPS)
            self.event_handler()
            self.update()
            self.draw()
