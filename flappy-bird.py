import pygame #biblioteca de geração de jogos
import os #biblioteca que integra o código com arquivos do computador
import random #os canos do jogo aparecem sempre de forma aleatória

TELA_LARGURA = 500 #constantes no Python são declaradas em letras maiúsculas
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png'))) #"os" junta (join) a pasta com o arquivo 
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND =  pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
#o pássaro na verdade é formado por uma lista de imagens
IMAGENS_PASSARO = [
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

#incializando e definindo a fonte a ser usada no texto de pontuação
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

#pássaro, canos e base são as coisas no jogo que se movem, por isso serão classes


class Passaro:
    IMGS = IMAGENS_PASSARO
    # animações da rotação




class Cano:
    pass




class Chao:
    pass

