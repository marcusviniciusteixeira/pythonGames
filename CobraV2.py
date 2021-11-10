import pygame
from pygame.locals import *
from random import randint

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

x = int(largura/2)
y = int(altura/2)

t = int(largura/3)
h = int(altura/2)

w = randint(30, (largura-20))
z = randint(30, (altura-20))

velocidade = 15
tamanhoPlayers = 15
tamanhoColisor = 10
fps = 30
pontos1 = pontos2 = 0

FUNDO = (50,50,50)
RED = (150,0,0)
BLUE = (0,0,150)
COR = (255,255,255)

#wav = pygame.mixer.Sound('Users\marqu\OneDrive\Documentos\projetos dev\w.wav')

def Aumentar(posicao1, posicao2):
    for XeY in posicao1:
        player1 = pygame.draw.circle(tela, RED, (XeY[0], XeY[1]), tamanhoPlayers)
    for TeH in posicao2:
        player2 = pygame.draw.circle(tela, BLUE, (TeH[0], TeH[1]), tamanhoPlayers)

posicao1 = []
posicao2 = []

while True:
    relogio.tick(fps)
    tela.fill(FUNDO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
#players
    player1 = pygame.draw.circle(tela, RED, (x, y), tamanhoPlayers)
    player2 = pygame.draw.circle(tela, BLUE, (t, h), tamanhoPlayers)

    colisor = pygame.draw.circle(tela, COR, (w,z), tamanhoColisor)
#movement
    #player1
    if pygame.key.get_pressed()[K_a]:
        x -= velocidade
    if pygame.key.get_pressed()[K_d]:
        x += velocidade
    if pygame.key.get_pressed()[K_w]:
        y -= velocidade
    if pygame.key.get_pressed()[K_s]:
        y += velocidade
    #player2
    if pygame.key.get_pressed()[K_LEFT]:
        t -= velocidade
    if pygame.key.get_pressed()[K_RIGHT]:
        t += velocidade
    if pygame.key.get_pressed()[K_UP]:
        h -= velocidade
    if pygame.key.get_pressed()[K_DOWN]:
        h += velocidade
    
#parede
    #player1
    if x < 0:
        x = largura
    if x > largura:
        x = 0
    if y < 0:
        y = altura
    if y > altura:
        y = 0
    #player2
    if t < 0:
        t = largura
    if t > largura:
        t = 0
    if h < 0:
        h = altura
    if h > altura:
        h = 0

#colisao
    if player1.colliderect(colisor):
        w = randint(30, (largura-20))
        z = randint(30, (altura-20))
        pontos1 += 1
        print(f'Pontos RED: {pontos1}')
        #wav.play()
        
    if player2.colliderect(colisor):
        w = randint(30, (largura-20))
        z = randint(30, (altura-20))
        pontos2 += 1
        print(f'Pontos BLUE: {pontos2}')
        #wav.play()
#listas        
    lista1 = []
    lista1.append(x)
    lista1.append(y)

    lista2 = []
    lista2.append(t)
    lista2.append(h)

    posicao1.append(lista1)
    posicao2.append(lista2)

#del cobra
    if len(posicao1) > 5:
        del posicao1[0]
    if len(posicao2) > 5:
        del posicao2[0]

    

    Aumentar(posicao1, posicao2)
    
    pygame.display.flip()