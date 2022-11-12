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
        self.screen_height = 800
        self.bg_color = (225, 225, 225)
        # Настройки корабля
        self.ship_speed = 1.5
