import pygame.font

class Button():

    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

