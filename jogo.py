import pygame
import random

pygame.mixer.init()
pygame.init()

#criando janela
screen_x = 440 * 2
screen_y = 250 * 2
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("PONG")
inicio = pygame.image.load('start.jpeg.jpg')
pygame.display.set_icon(inicio)
start_image = pygame.image.load("start.jpeg.jpg")
start_image = pygame.transform.scale2x(start_image)
clock = pygame.time.Clock()

background = pygame.image.load('fundo.jpeg.jpg')
background = pygame.transform.scale2x(background)

font = pygame.font.SysFont(None,45)
font_1 = pygame.font.SysFont(None,35)
text_font = pygame.font.Font(None,80)
times = 0
def font_screen(text,color, x, y):
    pong_text = font.render(text, True, color)
    screen.blit(pong_text, [x,y])

def font_screen_1(text,color,x,y):
    enter_text = font_1.render(text,True,color)
    screen.blit(enter_text, [x,y])

def welcome_screen():
    exit_game = False
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
#loop do jogo

def loop():
    times = 0
    alunoInsper_score = 0
    Vestibulando_score = 0
    alunoInsper_velocity = 0
    alunoInsper = pygame.Rect(5, screen_y / 2 - 70, 8, 130)
    Vestibulando_velocity= 0
    Vestibulando = pygame.Rect(screen_x - 12, screen_y/2-70, 8, 130)
    
    bola_velocity_x = 4*random.choice((1,-1))
    bola_velocity_y = 4*random.choice((1,-1))

    bola = bola_create(bola_velocity_x, bola_velocity_x)[0]
    bola.center = bola_create(bola_velocity_x, bola_velocity_x)[1]
    color = bola_create(bola_velocity_x, bola_velocity_x)[2]

    running = True
    inverte = False
    item_img = pygame.image.load("inverte.jpg").convert_alpha()
    item_img = pygame.transform.scale(item_img, (489//10,750//10))
    item = Fogo(item_img)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    loop()
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_PAUSE:
                    bola_velocity_x=0
                    bola_velocity_y=0
                if event.key == pygame.K_UP:
                    if inverte == False:
                        Vestibulando.y = Vestibulando.y-90
                    else:
                        Vestibulando.y = Vestibulando.y+90

                if event.key == pygame.K_DOWN:
                    if inverte == False:
                        Vestibulando.y = Vestibulando.y+90
                    else:
                        Vestibulando.y = Vestibulando.y-90

                if event.type == pygame.KEYDOWN:
                    if inverte == False:
                        if event.key == pygame.K_w:
                            alunoInsper.y = alunoInsper.y-90
                        if event.key == pygame.K_s:
                            alunoInsper.y = alunoInsper.y+90
                    else:
                        if event.key == pygame.K_w:
                            alunoInsper.y = alunoInsper.y+90
                        if event.key == pygame.K_s:
                            alunoInsper.y = alunoInsper.y-90

        alunoInsper.y = alunoInsper.y + alunoInsper_velocity
        if alunoInsper.y <bola.y:
           alunoInsper.top += alunoInsper_velocity
        if Vestibulando.bottom > bola.y:
            alunoInsper.bottom -= alunoInsper_velocity
        if alunoInsper.top <= 0 :
            alunoInsper.top = 0
        if alunoInsper.bottom >= screen_y:
           alunoInsper.bottom = screen_y

        Vestibulando.y = Vestibulando.y + Vestibulando_velocity
        if Vestibulando.top <= 0:
            Vestibulando.top = 0
        if Vestibulando.bottom >= screen_y:
            Vestibulando.bottom = screen_y
            
        bola.x = bola.x + bola_velocity_x
        bola.y = bola.y + bola_velocity_y
        agora=pygame.time.get_ticks()

        if agora-times>=5000:
            if bola_velocity_x>0:
                bola_velocity_x+=1
            else:
                bola_velocity_x-=1
            times=agora
            
        if bola.left <= 0 :
            if color == 'white':
                Vestibulando_score += 1
            else:
                Vestibulando_score += 2
            bola = bola_create(bola_velocity_x, bola_velocity_y)[0]
            bola.center = bola_create(bola_velocity_x, bola_velocity_y)[1]
            color = bola_create(bola_velocity_x, bola_velocity_y)[2]

        if bola.right >= screen_x:
            if color == 'white':
                alunoInsper_score += 1
            else:
                alunoInsper_score += 2
            bola = bola_create(bola_velocity_x, bola_velocity_y)[0]
            bola.center = bola_create(bola_velocity_x, bola_velocity_y)[1]
            color = bola_create(bola_velocity_x, bola_velocity_y)[2]

        if bola.top <= 0 or bola.bottom >= screen_y:
            pygame.mixer.music.load("BOUNCEsound.mp3")
            pygame.mixer.music.play()
            bola_velocity_y = bola_velocity_y*-1
            inverte=False

        if bola.colliderect(alunoInsper) or bola.colliderect(Vestibulando):
            pygame.mixer.music.load("BOUNCEsound.mp3")
            pygame.mixer.music.play()
            bola_velocity_x = bola_velocity_x*-1
        if bola.colliderect(item.rect):
            inverte=True

        screen.blit(background, (0, 0))
        
        screen.blit(item.image,item.rect)
        pygame.draw.ellipse(screen, pygame.Color(color), bola)
        pygame.draw.rect(screen, pygame.Color(color), alunoInsper)
        pygame.draw.rect(screen, pygame.Color(color), Vestibulando)
        pygame.draw.aaline(screen, pygame.Color(color), (screen_x/2, 0), (screen_x/2, screen_y))

        score_text = text_font.render(f"{alunoInsper_score}", True, pygame.Color(color))
        screen.blit(score_text, (165, 10))
        score_text = text_font.render(f"{Vestibulando_score}", True, pygame.Color(color))
        screen.blit(score_text, (520, 10))
        if alunoInsper_score == 10:
            bola_velocity_x = 0
            bola_velocity_y = 0
            font_screen("alunoInsper WON", pygame.Color('white'), 68, 200)
            font_screen_1("Play Again!!Press P", pygame.Color('white'), 68, 250)
        if Vestibulando_score == 10:
            bola_velocity_x = 0
            bola_velocity_y = 0
            font_screen("Vestibulando WON", pygame.Color('white'), 395, 200)
            font_screen_1("Play Again!!Press P", pygame.Color('white'), 395, 250)

        pygame.display.update()
        clock.tick(75)
    pygame.quit()
    quit()
welcome_screen()
