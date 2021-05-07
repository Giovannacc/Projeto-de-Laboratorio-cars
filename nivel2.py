import pygame
import random
import sys
from function import *
from config import *
from carro import *
from carroinimigo import *
from buraco import *
from gameover import *
from pygame.locals import *


def main2(screen):
    imagem_1 = pygame.image.load(IMAGEM_BACKGROUND2)
    imagem_2 = pygame.image.load(IMAGEM_BACKGROUND2)
    posicao_y = 0
    musica(1)
    carro = Carro(screen)

    carros_inimigos = []
    for i in range(QUANTIDADE_INIMIGO):
        posicao_na_pista = local_pista()
        carros_inimigos.append(CarroInimigo(screen, posicao_na_pista, -150))

    posicao_buraco = local_pista()
    buraco = Buraco(screen, posicao_buraco, 0)

    score = 0
    cont_score = 0
    cont_colide = 0
    background_speed = 5

    clock = pygame.time.Clock()

    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_janela()

        tecla = pygame.key.get_pressed()

        mover_backgroud(screen, imagem_1, imagem_2, posicao_y)
        posicao_y += background_speed
        if posicao_y >= RESOLUCAO[1]:
            posicao_y = 0

        # PONTUAÇÃO #
        cont_score += 1
        if cont_score % 4 == 0:
            score += 1

        imprime_texto(screen, "SCORE", (450, 10), FONTE_PIXEL, BRANCO)
        imprime_texto(screen, score, (479, 35), FONTE_DG, BRANCO)

        imprime_texto(screen, "VIDA", (7, 10), FONTE_PIXEL, PRETO)
        imprime_texto(screen, carro.life, (30, 35), FONTE_DG, PRETO)

        if score >= 400:
            buraco.render()
            buraco.move()

        carro.render()
        carro.mover_carro(tecla)

        for inimigo in carros_inimigos:
            inimigo.render()
            inimigo.move()
            # COLISAO ENTRE OS CARROS INIMIGOS E O CARRO #
            if carro.rect_car.colliderect(inimigo.rect_carro):
                salvar_score(score)
                musica(0)
                game_over(screen, score)

        # COLISAO ENTRE OS CARROS INIMIGOS #
        if carros_inimigos[0].rect_carro.colliderect(carros_inimigos[1].rect_carro):
            carros_inimigos[0].x = carros_inimigos[0].pista[random.randint(0, 2)]
            carros_inimigos[0].y = -150

        # COLISAO ENTRE OS BURRACOS NA PISTA #
        colide = False
        if carro.rect_car.colliderect(buraco.rect_buraco) and score >= 400:
            colide = True
            cont_colide += 1

        temp_maximo = 20
        if colide == True and cont_colide > temp_maximo:
            carro.life -= 1
            cont_colide = 0
            colide = False

        if carro.life == 0:
            salvar_score(score)
            musica(0)
            game_over(screen, score)

        aumentar_velocidade(score, carros_inimigos, carro, background_speed, temp_maximo)

        pygame.display.flip()
        clock.tick(FPS)
