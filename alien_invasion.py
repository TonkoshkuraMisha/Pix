import sys

import pygame
bg = pygame.image.load("img\\bg.png")

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Pix's Adventures")
        programIcon = pygame.image.load('img\pix.png')
        pygame.display.set_icon(programIcon)
        # Назначение цвета фона.
        # self.bg_color = (20, 250, 70)


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # При каждом проходе цикла перерисовывается экран.
            self.screen.blit(bg, (0, 0))
            # self.screen.fill(self.bg_color)
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    pa = AlienInvasion()
    pa.run_game()
