import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 1000
altura = 800
x = largura/2
y = altura/2

w = largura/3
z = altura/2

Xcircle = randint(40, 600)#TAMANHO TELA
Ycircle = randint(50, 400)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(('meliodas'))
relogio = pygame.time.Clock()

contador1 = 0
contador2 = 0
fonte = pygame.font.SysFont('arial', 30, True, True)

#wav = pygame.mixer.Sound('')

while True:
    relogio.tick(20)
    tela.fill((255,255,255))
    mensagem1 = ('Pontos:{}'.format(contador1))
    mensagem2 = ('Pontos:{}'.format(contador2))
    textoFormat1 = fonte.render(mensagem1, True, (0,255,0))
    textoFormat2 = fonte.render(mensagem2, True, (0,0,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''    
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
        '''
    if pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 20

    if pygame.key.get_pressed()[K_a]:
        w = w - 20
    if pygame.key.get_pressed()[K_d]:
        w = w + 20
    if pygame.key.get_pressed()[K_w]:
        z = z - 20
    if pygame.key.get_pressed()[K_s]:
        z = z + 20

    player1 = pygame.draw.rect(tela, (0,255,0), (x,y,40,50))
    player2 = pygame.draw.rect(tela, (0,0,255), (w,z,40,50))
    
    colisor = pygame.draw.circle(tela, (255,0,0), (Xcircle,Ycircle,), 10)

    if player1.colliderect(colisor) or player2.colliderect(colisor):
        Xcircle = randint(40, 600)
        Ycircle = randint(50, 430)

    if player1.colliderect(colisor):
        contador1 = contador1 + 1 
        print('Player Vermelho:{}'.format(contador1))
        #wav.play()  

    if player2.colliderect(colisor):
        contador2 = contador2 + 1
        print('Player Azul:{}'.format(contador2))
        #wav.play()
    
    if x > largura:
        x = 0 
    if x < 0:
        x = largura 
    if y > altura:
        y = 0 
    if y < 0:
        y = altura

    if w > largura:
        w = 0 
    if w < 0:
        w = largura 
    if z > altura:
        z = 0 
    if z < 0:
        z = altura
    
    tela.blit(textoFormat1, (450,40))
    tela.blit(textoFormat2, (40,40))
    #pygame.draw.line(tela, (96,0,189),(390,0),(390,600),5)
    pygame.display.update()






