import pygame


class Ship():
    """Класс управления кораблём."""

    def __init__(self, pa_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = pa_game.screen
        self.screen_rect = pa_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
