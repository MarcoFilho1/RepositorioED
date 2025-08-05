# -*- coding: utf-8 -*-
import time
from maze import Maze

# Cria o labirinto
maze = Maze()

# Carrega o mapa
maze_csv_path = "labirinto1.txt"
maze.load_from_csv(maze_csv_path)

# Inicia a visualização 
maze.run()

maze.init_player()

start_pos = maze.get_init_pos_player()

# Criar pilha e conjunto de visitados
pilha = []
visitados = set()

# Insere as posiçoes iniciais na pilha
pilha.append(start_pos)
visitados.add(start_pos)

# Movimentos possíveis: cima, baixo, esquerda, direita
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Algoritmo de backtracking com pilha
while pilha:
    
    pos = pilha.pop()
    maze.mov_player(pos)
    time.sleep(0.02)

    # Se encontrou o prêmio, encerra
    if maze.find_prize(pos):
        print("Caminho encontrado!")
        break

    # Verifica vizinhos e empilha os que forem livres e não visitados
    for mov in movimentos:
        nova_pos = (pos[0] + mov[0], pos[1] + mov[1])
        if nova_pos not in visitados and maze.is_free(nova_pos):
            pilha.append(nova_pos)
            visitados.add(nova_pos)
else:
    print("Nao foi possivel encontrar o premio.")
