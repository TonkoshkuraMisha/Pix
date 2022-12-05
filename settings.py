import pygame

# bg = pygame.image.load("src/img/si_logo.png")
programIcon = pygame.image.load('src/img/pix.png')
pygame.display.set_icon(programIcon)


class Settings():
    """Класс для настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (100, 100, 100)
        # Настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 500
        self.bullet_height = 25
        self.bullet_color = (26, 217, 24)
        self.bullets_allowed = 1
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1


