import pygame

# bg = pygame.image.load("img\\bg.png")
programIcon = pygame.image.load('img/pix.png')
pygame.display.set_icon(programIcon)


class Settings():
    """Класс для настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 0, 0)
