# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
    def tem_campeao(self):
        result = 0
        result_columns = 0
        # Verifica se há linhas ou colunas  vencedoras
        for i in range(0,3):
            for j in range(0,3):
                result += self.matriz[i][j]
                result_columns += self.matriz[j][i]
                if result == 3 or result_columns == 3:
                    return Tabuleiro.JOGADOR_0
                elif result == 12 or result_columns == 12:
                    return Tabuleiro.JOGADOR_X
            result=0
            result_columns=0

        # Verifica a diagonal principal
        for i in range(0,3):
            result += self.matriz[i][i]
            if result == 3:
                return Tabuleiro.JOGADOR_0
            elif result == 12:
                return Tabuleiro.JOGADOR_X
        
        # Verifica a diagonal secundaria
        result = 0
        for i in range(0,3):
            reversed_tabuleiro = self.matriz[::-1]
            result += reversed_tabuleiro[i][i]
            if result == 3:
                return Tabuleiro.JOGADOR_0
            elif result == 12:
                return Tabuleiro.JOGADOR_X


        # Verifica colunas
        """result = 0
        for i in range(0,3):
            for j in range(0,3):
                result += self.matriz[j][i]
                if result == 3:
                    return Tabuleiro.JOGADOR_0
                elif result == 12:
                    return Tabuleiro.JOGADOR_X
            result=0"""
