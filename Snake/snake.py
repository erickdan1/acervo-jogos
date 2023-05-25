import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
# para estabelecer o volume: (entre 0 e 1)
pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer.music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)
# com exceçao do arquivo da musica de fundo todos os outro devem ter essa extensão:(wav)
som_colisao = pygame.mixer.Sound('smw_coin.wav')
som_colisao.set_volume(0.3)
# variaveis para controlar movimento
x_cobra = int(largura / 2 - 30 / 2)
y_cobra = int(altura / 2 - 30 / 2)

velocidade = 5
# evitar que a cobra vire para diagonal
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
# parametros => estilo, tamanho, negrito, italico
fonte = pygame.font.SysFont('arial', 25, True, False)

# definicao do tamanho da tela
tela = pygame.display.set_mode((largura, altura))
# definicao do nome exibido
pygame.display.set_caption('joguin daora da cobrinha')

# controlar a taxa de frames do jogo para contolara a velocidade do obj
clock = pygame.time.Clock()


# funcao que desenha o corpo da cobra
def cresce_cobra(lista_cobra):
    for x, y in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (x, y, 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2 - 30 / 2)
    y_cobra = int(altura / 2 - 30 / 2)
    lista_cobra = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


lista_cobra = []
comprimento_inicial = 5
morreu = False

while True:
    clock.tick(40)
    # preenche a tela e evita que o movimento deixe rastro
    tela.fill((0, 0, 0))
    mensagem = f'Pontuação: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    for event in pygame.event.get():
        # para a fechar a execucao
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra += x_controle
    y_cobra += y_controle

    '''
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 10
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 10
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 10
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 10'''

    # parametros(onde sera desenhado, cor, (posicaoX, posicaoY, largura do obj, altura do obj))
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    
    # condicao de colisao
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        som_colisao.play()
        comprimento_inicial += 3
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    # caso a cobra encoste nela mesma
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 13, True, False)
        mensagem2 = 'GAME OVER! Pressione R para jogar novamente'
        texto_formatado2 = fonte.render(mensagem2, True, (255, 255, 255))
        retangulo_texto = texto_formatado2.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            retangulo_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado2, retangulo_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    cresce_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()
