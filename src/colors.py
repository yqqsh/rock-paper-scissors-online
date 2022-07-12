from pygame.colordict import THECOLORS

for name, value in THECOLORS.items():
    locals()[name] = value
