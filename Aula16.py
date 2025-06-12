# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




# VARIÁVEL QUE ARMAZENA A LARGURA E ALTURA 
largura, altura = 400, 400
# VARIACEL QUE ATRIBUI A LARGURA E ALTURA DA TELA
tela = pygame.display.set_mode((largura, altura))
# TITULO DA TELA
pygame.display.set_caption("Labirinto")

# TUPLA PARA AS CORES 
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# LISTA PARA DEFINIR O LABIRINTO    
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# VARIÁVEL PARA DEFINIR O TAMANHO DA CÉLULA
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40

#DESENHAR O LABIRINTO
def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
# VARIÁVEL QUE ATRIBUI UMA LISTA 
            cor = preto if labirinto[linha][coluna] == 1 else branco
# DESENHANDO UM RETANGULO NA TELA
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# LOOP
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

# VARIÁVEL PARA TECLAS
    teclas = pygame.key.get_pressed()
# CONDICIONAL PARA A TECLA DA ESQUERDA
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
# CONDICIONAL PARA A TECLA DA DIREITA
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
# CONDICIONAL PARA A TECLA PARA CIMA 
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
# CONDICIONAL PARA A TECLA PARA BAIXO
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

# COMANDO PARA MUDAR A COR DA TELA
    tela.fill(branco)

# COMANDO PARA DESENHAR O LABIRINTO
    desenhar_labirinto()
# DESENHANDO UM RETANGULO
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

# ATUALIZAR A TELA
    pygame.display.flip()

# CONTAGEM DE QUADROS
    pygame.time.Clock().tick(10)


pygame.quit()


