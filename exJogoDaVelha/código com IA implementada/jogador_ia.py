# -*- coding: utf-8 -*-
from random import randint
from random import choice
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            


    def get_casas_vazias(self):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        return lista



    def get_linhas_by_coordinates(self):
        linhas   = [[(r, c) for c in range(3)] for r in range(3)]
        colunas  = [[(r, c) for r in range(3)] for c in range(3)]
        diagonais = [[(0, 0), (1, 1), (2, 2)],
                    [(0, 2), (1, 1), (2, 0)]]
        return linhas + colunas + diagonais


    # Funçao para a regra 1:
    def bloquear_linha_com_duas(self, marca):
        for linha in self.get_linhas_by_coordinates():
            marcas = [self.matriz[l][c] for l, c in linha]

            if marcas.count(marca) == 2 and marcas.count(Tabuleiro.DESCONHECIDO) == 1:
                index_vazio = marcas.index(Tabuleiro.DESCONHECIDO)
                return linha[index_vazio]
            
        return None



    # Funçao para a regra 2
    def cria_fork(self):
        for linha, coluna in self.get_casas_vazias():
            # Simula a jogada
            self.matriz[linha][coluna] = self.tipo
            jogadas_possiveis = 0

            # Conta quantas linhas ficariam com duas peças e um vazio
            for coordenadas in self.get_linhas_by_coordinates():
                linha_atual = [self.matriz[l][c] for l,c in coordenadas]
                if linha_atual.count(self.tipo) == 2 and linha_atual.count(Tabuleiro.DESCONHECIDO) == 1:
                    jogadas_possiveis += 1

            # Desfaz a jogada 
            self.matriz[linha][coluna] = Tabuleiro.DESCONHECIDO

        if jogadas_possiveis >= 2:
            return (linha, coluna)
        
        return None


    # Funçao para a regra 3:
    def centro(self):
        coord = self.matriz[1][1]
        if coord == Tabuleiro.DESCONHECIDO:
            return (1,1)
        return None
    


    # Funçao para a regra 4
    def canto_oposto(self):

        cantos_opostos =  {
        (0, 0): (2, 2),
        (0, 2): (2, 0),
        (2, 0): (0, 2),
        (2, 2): (0, 0)
        }

        for canto, oposto in cantos_opostos.items():
            linha1, coluna1 = canto
            linha2, coluna2 = oposto

            if self.matriz[linha1][coluna1] == Tabuleiro.JOGADOR_X and self.matriz[linha2][coluna2] == Tabuleiro.DESCONHECIDO:
                return oposto
            
        return None


    # R5
    def casa_aleatorio(self):
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                    
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        

    # Funçao utilizando todas as regras:
    def getJogada(self) -> (int, int):
        # R1 
        jog = self.bloquear_linha_com_duas(self)
        if not jog:
            jog = self.bloquear_linha_com_duas(Tabuleiro.JOGADOR_X)
        if jog:
            return jog
        
        # R2 - criar fork
        jog = self.cria_fork()
        if jog:
            return jog
        
        # R3 - centro
        jog = self.centro()
        if jog:
            return jog
        
        # R4 - canto oposto
        jog = self.canto_oposto()
        if jog:
            return jog
        
        # R5 - canto vazio
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        cantos_disponiveis = [pos for pos in cantos
        if self.matriz[pos[0]][pos[1]] == Tabuleiro.DESCONHECIDO]
        if cantos_disponiveis:
            return choice(cantos_disponiveis)
        
        # R6 - qualquer casa vazio
        jog = self.casa_aleatorio()
        if jog:
            return jog
        

