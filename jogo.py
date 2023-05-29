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
def font_screen(text,color, x, y):
    pong_text = font.render(text, True, color)
    screen.blit(pong_text, [x,y])

def font_screen_1(text,color,x,y):
    enter_text = font_1.render(text,True,color)
    screen.blit(enter_text, [x,y])

def welcome_screen():
    exit_game= False
    while not exit_game:
        screen.blit(start_image, [0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    loop()
        pygame.display.update()
        clock.tick(60)
class Fogo(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 700)
        self.rect.y = random.randint(0,400)
  #criando bola

def bola_create(bola_velocity_x,bola_velocity_y):

    bola_x = screen_x/2-15
    bola_y = screen_y/2-15
    bola = pygame.Rect(bola_x,bola_y, 25, 25)

    bola.center= (screen_x/2,screen_y/2)
    bola_velocity_x *= random.choice((1,-1))
    bola_velocity_y *= random.choice((1,-1))

    prob = random.randint(0, 8)
    if prob == 1:
        color = 'orange'
    else:
        color = 'white'
    
    return [bola, bola.center, color]     