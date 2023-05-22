import pygame

pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bolinha")
clock = pygame.time.Clock()
FPS = 240
	
background = pygame.image.load("fundo.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))