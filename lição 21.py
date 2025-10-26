import pygame
pygame.init()
pygame.mixer.music.load("jazz.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()