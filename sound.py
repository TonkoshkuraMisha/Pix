from pygame import mixer


class Sound():
    """Класс для настроек звуков игры"""

    def __init__(self):
        """Инициализирует звуки игры"""
        # Starting the mixer
        mixer.init()
        # Loading the song
        mixer.music.load("src/sounds/spaceinvaders1.mp3")
        # Setting the volume
        mixer.music.set_volume(0.1)
        # Start playing the song
        mixer.music.play(-1)
