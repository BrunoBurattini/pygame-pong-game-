import pygame
import random

pygame.mixer.init()
pygame.init()

#criando janela
screen_x = 440 * 2
screen_y = 250 * 2
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("PONG")
inicio= pygame.image.load('start.jpeg.jpg')
pygame.display.set_icon(inicio)
start_image= pygame.image.load("start.jpeg.jpg")
start_image = pygame.transform.scale2x(start_image)
clock= pygame.time.Clock()

background = pygame.image.load('fundo.jpeg.jpg')
background = pygame.transform.scale2x(background)

font = pygame.font.SysFont(None,45)
font_1 = pygame.font.SysFont(None,35)
text_font=pygame.font.Font(None,80)
times = 0