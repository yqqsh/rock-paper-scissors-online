import pygame
import src.config as cfg


class Button:
    def __init__(self, x, y, w, h, image=None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = image

    def draw(self, color) -> None:
        return self.draw_to(cfg.get_main_surface(), color)

    def draw_to(self, surface, color) -> None:
        if self.image == None:
            pygame.draw.rect(surface, color, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def is_over(self, pos) -> bool:
        return self.rect.collidepoint(pos)

    def is_clicked(self, event) -> bool:
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_over(event.pos)
