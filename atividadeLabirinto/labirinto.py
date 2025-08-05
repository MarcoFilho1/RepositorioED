# -*- coding: utf-8 -*-
import pygame
import random
import sys

# Configurações
LARGURA = 600
ALTURA = 600
TAMANHO_CELULA = 20
COLS = LARGURA // TAMANHO_CELULA
ROWS = ALTURA // TAMANHO_CELULA

# Cores
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto Backtracking")

clock = pygame.time.Clock()

def gerar_labirinto():
    lab = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLS):
            if random.random() < 0.25:
                lab[y][x] = 1
    for x in range(COLS):
        lab[0][x] = 1
        lab[ROWS-1][x] = 1
    for y in range(ROWS):
        lab[y][0] = 1
        lab[y][COLS-1] = 1
    return lab

def desenhar_labirinto(lab, jogador, premio, visitados):
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x*TAMANHO_CELULA, y*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            if lab[y][x] == 1:
                pygame.draw.rect(tela, PRETO, rect)
            else:
                pygame.draw.rect(tela, CINZA, rect)

            if (y, x) in visitados:
                pygame.draw.rect(tela, AZUL, rect)

    pygame.draw.rect(tela, AMARELO, (premio[1]*TAMANHO_CELULA, premio[0]*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
    pygame.draw.rect(tela, VERMELHO, (jogador[1]*TAMANHO_CELULA, jogador[0]*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

    pygame.display.flip()

def tem_vizinhos_livres(pos, lab, visitados):
    movimentos = [(-1,0), (1,0), (0,-1), (0,1)]
    for mov in movimentos:
        ny = pos[0] + mov[0]
        nx = pos[1] + mov[1]
        if 0 <= ny < ROWS and 0 <= nx < COLS:
            if lab[ny][nx] == 0 and (ny, nx) not in visitados:
                return True
    return False

def resolver_labirinto(lab, inicio, premio):
    caminho_atual = [inicio]
    visitados = set([inicio])
    movimentos = [(-1,0), (1,0), (0,-1), (0,1)]

    while caminho_atual:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pos = caminho_atual[-1]

        if pos == premio:
            print("Caminho encontrado!")
            return True

        vizinhos_livres = []
        for mov in movimentos:
            ny = pos[0] + mov[0]
            nx = pos[1] + mov[1]
            if 0 <= ny < ROWS and 0 <= nx < COLS:
                if lab[ny][nx] == 0 and (ny, nx) not in visitados:
                    vizinhos_livres.append((ny, nx))

        if vizinhos_livres:
            proximo = vizinhos_livres[0]
            caminho_atual.append(proximo)
            visitados.add(proximo)
        else:
            # Teleporte: acha ponto da cauda com vizinhos livres
            for i in range(len(caminho_atual)-1, -1, -1):
                if tem_vizinhos_livres(caminho_atual[i], lab, visitados):
                    caminho_atual = caminho_atual[:i+1]
                    break
            else:
                break  # acabou

        tela.fill((255,255,255))
        desenhar_labirinto(lab, caminho_atual[-1], premio, visitados)
        clock.tick(20)

    return False

def posicao_aleatoria(lab):
    while True:
        y = random.randint(1, ROWS-2)
        x = random.randint(1, COLS-2)
        if lab[y][x] == 0:
            return (y, x)

labirinto = gerar_labirinto()
jogador = posicao_aleatoria(labirinto)
premio = posicao_aleatoria(labirinto)

resolver_labirinto(labirinto, jogador, premio)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
