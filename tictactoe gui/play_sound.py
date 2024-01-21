import pygame

class PlaySound:
    def __init__(self) -> None:
        self.button_click = "audio_files/button.mp3"
        self.over = "audio_files/over.mp3"
        self.each_click = "audio_files/click.mp3"

    def game_over(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.over) 
        sound.play()

    def click_noise(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.each_click) 
        sound.play()

    def button_noise(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.button_click) 
        sound.play()


