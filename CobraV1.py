import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 420
x = largura/2
y = altura/2
w = largura/3
z = altura/2

velocidade = 7
Xcontrole = velocidade
Ycontrole = 0
Wcontrole = velocidade
Zcontrole = 0

death = False

Xcircle = randint(40, 600)#TAMANHO TELA
Ycircle = randint(50, 430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(('Apple Snake'))
relogio = pygame.time.Clock()

contador1 = 0
contador2 = 0
fonte = pygame.font.SysFont('arial', 30, True, True)

posição = []
lista_cobra = []

comprInicial = 5
comprInicial2 = 5

wav = pygame.mixer.Sound('projetos dev\w.wav')

def tamCobra(posição):
    for XeY in posição:
        player1 = pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def aumenta_cobra(lista_cobra):
    for WeZ in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        player2 = pygame.draw.rect(tela, (0,0,255), (WeZ[0], WeZ[1], 20, 20))
'''
def restart():
    global contador1, contador2, comprInicial, x,y,w,z,posição, lista, Xcircle, Ycircle, death 
    contador1 = 0
    contador2 = 0
    comprInicial = 5
    x = largura/2
    y = altura/2
    w = largura/3
    z = altura/2
    posição = []
    lista = []
    Xcircle = randint(40, 630)
    Ycircle = randint(50, 400)
    death = False
'''
while True:
    relogio.tick(30)#frames
    tela.fill((255,255,255))#tela branca
    mensagem1 = ('Pontos:{}'.format(contador1))
    mensagem2 = ('Pontos:{}'.format(contador2))
    textoFormat1 = fonte.render(mensagem1, True, (0,255,0))#pontos
    textoFormat2 = fonte.render(mensagem2, True, (0,0,255))#pontos2
    for event in pygame.event.get():#quit
        if event.type == QUIT:
            pygame.quit()
            exit()
    #movement    
        if event.type == KEYDOWN:
            if event.key == K_a:
                if Xcontrole == velocidade:
                    pass
                else:
                    Xcontrole = -velocidade
                    Ycontrole = 0
            if event.key == K_d:
                if Xcontrole == -velocidade:
                    pass
                else:
                    Xcontrole = velocidade
                    Ycontrole = 0
            if event.key == K_w:
                if Ycontrole == velocidade:
                    pass
                else:
                    Ycontrole = -velocidade
                    Xcontrole = 0
            if event.key == K_s:
                if Ycontrole == -velocidade:
                    pass
                else:
                    Ycontrole = velocidade
                    Xcontrole = 0

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if Wcontrole == velocidade:
                    pass
                else:
                    Wcontrole = -velocidade
                    Zcontrole = 0
            if event.key == K_RIGHT:
                if Wcontrole == -velocidade:
                    pass
                else:
                    Wcontrole = velocidade
                    Zcontrole = 0
            if event.key == K_UP:
                if Zcontrole == velocidade:
                    pass
                else:
                    Zcontrole = -velocidade
                    Wcontrole = 0
            if event.key == K_DOWN:
                if Zcontrole == -velocidade:
                    pass
                else:
                    Zcontrole = velocidade
                    Wcontrole = 0

    x = x + Xcontrole
    y = y + Ycontrole
    w = w + Wcontrole
    z = z + Zcontrole

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
    '''
    #player and colisor
    player1 = pygame.draw.rect(tela, (0,255,0), (x,y,20,20))
    player2 = pygame.draw.rect(tela, (0,0,255), (w,z,20,20))
    
    colisor = pygame.draw.circle(tela, (255,0,0), (Xcircle,Ycircle,), 9)
    
    if player1.colliderect(colisor):
        Xcircle = randint(40, 600)
        Ycircle = randint(50, 430)
        comprInicial = comprInicial + 1
    
    if player2.colliderect(colisor):
        Xcircle = randint(40, 600)
        Ycircle = randint(50, 430)
        comprInicial2 = comprInicial2 + 1
    

    if player1.colliderect(colisor):
        contador1 = contador1 + 1 
        wav.play()  

    if player2.colliderect(colisor):
        contador2 = contador2 + 1
        wav.play()
    #listas posições
    lista = []
    lista.append(x)
    lista.append(y)

    posição.append(lista)

    lista_cabeca = []
    lista_cabeca.append(w)
    lista_cabeca.append(z)
    
    lista_cobra.append(lista_cabeca)

        
    '''
    if posição.count(lista) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.flip()    
    '''
    #final tela
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
    #exclui lista quando reiniciado                
    if len(posição) > comprInicial:
        del posição[0]

    tamCobra(posição)

    if len(lista_cobra) > comprInicial2:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    
    #pontos para = break
    if contador1 == 100:
        break
    if contador2 == 100:
        break

    #texto pontos
    tela.blit(textoFormat1, (450,40))
    tela.blit(textoFormat2, (40,40)) 
    #pygame.draw.line(tela, (96,0,189),(390,0),(390,600),5)

    pygame.display.flip()






