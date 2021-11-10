import pygame
from pygame.locals import *
from sys import exit
from random import randint
 
pygame.init()

largura = 800
altura = 600

x = int(largura/2)
y = int(altura/2)
 
t = int(largura/3) 
h = int(altura/2) 

w = int(largura/4) 
z = int(altura/2)

Xcolisor = randint(30, largura)
Ycolisor = randint(30, altura)

Tcolisor = randint(30, largura)
Hcolisor = randint(30, altura)

Wcolisor = randint(30, largura)
Zcolisor = randint(30, altura)

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 30 , True, True)
velocidade = 10
tamanho = 20
tamanhoCircle = 7
tamanhoInicial1 = tamanhoInicial2 = tamanhoInicial3 = 5

ponto1 = ponto2 = ponto3 = 0

CINZA = (123,123,123)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

posicao1 = []
posicao2 = []
posicao3 = []

def Tam(posicao1, posicao2, posicao3):
    for XeY in posicao1:
        player1 = pygame.draw.rect(tela, RED, (XeY[0], XeY[1], tamanho, tamanho))
    for TeH in posicao2:
        player2 = pygame.draw.rect(tela, GREEN, (TeH[0], TeH[1], tamanho, tamanho))
    for WeZ in posicao3:
        player3 = pygame.draw.rect(tela, BLUE, (WeZ[0], WeZ[1], tamanho, tamanho))

while True:
    t1 = (f'Pontos: {ponto1}')
    t2 = (f'Pontos: {ponto2}')
    t3 = (f'Pontos: {ponto3}')
    tf1 = fonte.render(t1, True, RED)
    tf2 = fonte.render(t2, True, GREEN)
    tf3 = fonte.render(t3, True, BLUE)
    relogio.tick(30)
    tela.fill(CINZA)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    player1 = pygame.draw.rect(tela, RED, (x, y , tamanho, tamanho))
    player2 = pygame.draw.rect(tela, GREEN, (t, h , tamanho, tamanho))
    player3 = pygame.draw.rect(tela, BLUE, (w, z , tamanho, tamanho))

    colisor1 = pygame.draw.circle(tela, RED , (Xcolisor, Ycolisor), tamanhoCircle)
    colisor2 = pygame.draw.circle(tela, GREEN , (Tcolisor, Hcolisor), tamanhoCircle)
    colisor3 = pygame.draw.circle(tela, BLUE , (Wcolisor, Zcolisor), tamanhoCircle)

    if pygame.key.get_pressed()[K_a]:
        x -= velocidade
    if pygame.key.get_pressed()[K_d]:
        x += velocidade
    if pygame.key.get_pressed()[K_w]:
        y -= velocidade
    if pygame.key.get_pressed()[K_s]:
        y += velocidade

    if pygame.key.get_pressed()[K_LEFT]:
        t -= velocidade
    if pygame.key.get_pressed()[K_RIGHT]:
        t += velocidade
    if pygame.key.get_pressed()[K_UP]:
        h -= velocidade
    if pygame.key.get_pressed()[K_DOWN]:
        h += velocidade

    if pygame.key.get_pressed()[K_j]:
        w -= velocidade
    if pygame.key.get_pressed()[K_l]:
        w += velocidade
    if pygame.key.get_pressed()[K_i]:
        z -= velocidade
    if pygame.key.get_pressed()[K_k]:
        z += velocidade

    if player1.colliderect(colisor1):
        Xcolisor = randint(30, largura)
        Ycolisor = randint(30, altura)
        ponto1 += 1
        tamanhoInicial1 += 1
    if player2.colliderect(colisor2):
        Tcolisor = randint(30, largura)
        Hcolisor = randint(30, altura)
        ponto2 += 1
        tamanhoInicial2 += 1
    if player3.colliderect(colisor3):
        Wcolisor = randint(30, largura)
        Zcolisor = randint(30, altura)
        ponto3 += 1
        tamanhoInicial3 += 1

    if x < 0:
        x = largura
    if x > largura:
        x = 0
    if y < 0:
        y = altura
    if y > altura:
        y = 0

    if t < 0:
        t = largura
    if t > largura:
        t = 0
    if h < 0:
        h = altura
    if h > altura:
        h = 0

    if w < 0:
        w = largura
    if w > largura:
        w = 0
    if z < 0:
        z = altura
    if z > altura:
        z = 0

    #listas
    lista1 = []
    lista1.append(x)
    lista1.append(y)
    lista2 = []
    lista2.append(t)
    lista2.append(h)
    lista3 = []
    lista3.append(w)
    lista3.append(z)

    posicao1.append(lista1)
    posicao2.append(lista2)
    posicao3.append(lista3)

    if len(posicao1) > tamanhoInicial1:
        del posicao1[0]
    if len(posicao2) > tamanhoInicial2:
        del posicao2[0]
    if len(posicao3) > tamanhoInicial3:
        del posicao3[0]

    Tam(posicao1, posicao2, posicao3)

    tela.blit(tf1, (10,20))
    tela.blit(tf2, (330,20))
    tela.blit(tf3, (650,20))

    pygame.display.flip()