import pygame

class PlaySound:
    def __init__(self) -> None:
        self.eat = "eat_noise.mp3"
        self.over = "game_over.wav"
        self.move = "move_noise.wav"
        self.beep = "beep.wav"

    def eat_noise(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.eat) 
        sound.play()
        #pygame.time.wait(int(sound.get_length() * 1000))  # Wait for the sound to finish playing

    def game_over(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.over) 
        sound.play()

    def move_noise(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.move) 
        sound.play()

    def beep_noise(self):
        pygame.init()
        sound = pygame.mixer.Sound(self.beep) 
        sound.play()

