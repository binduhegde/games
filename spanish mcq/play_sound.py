import pygame

def happy_sound():
    pygame.init()
    sound = pygame.mixer.Sound("audios/happy.wav")
    sound.play()

def sad_sound():
    pygame.init()
    sound = pygame.mixer.Sound("audios/sad.wav")
    sound.play()
