import time
import os


def InsertionSort(lista, n):
    pivo = 0
    for i in range(0,n):
        pivo = lista[i]
        j = i-1
        while j >= 0 and lista[j] > pivo:
            lista[j+1] = lista[j]
            j = j-1
            lista[j+1] = pivo
    return lista

def SelectionSort(lista, n):
    for i in range(0,n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
            
        if lista[i] != lista[indice_minimo]:
            auxiliar = lista[i]
            lista[i] = lista[indice_minimo]
            lista[indice_minimo] = auxiliar
    return lista

def ler_arquivo(caminho):
    with open(caminho, "r") as f:
        return list(map(int, f.read().split()))


pasta = "exOrdenacoesQuadraticas/instancias-num"

# Listas que armazenam o resultado
results_insert = []
results_selection = []

# Loop para ler todos os arquivos e salvar em uma matriz
for nome_arquivo in os.listdir(pasta):
    caminho_completo = os.path.join(pasta, nome_arquivo)
    dados = ler_arquivo(caminho_completo)
    n = len(dados)

    print(f"\nArquivo: {nome_arquivo}")
    
    # InsertionSort
    copia_dados1 = dados.copy()
    inicio_insert = time.time()
    InsertionSort(copia_dados1, n)
    fim_insert = time.time()
    tempo_insert = fim_insert - inicio_insert
    results_insert.append((nome_arquivo, tempo_insert))
    print("InsertionSort: ", tempo_insert, "segundos")

    # SelectionSort
    copia_dados2 = dados.copy()
    inicio_select = time.time()
    SelectionSort(copia_dados2, n)
    fim_select = time.time()
    tempo_select = fim_select - inicio_select
    results_selection.append((nome_arquivo, tempo_select))
    print("SelectionSort:  ", tempo_select, "segundos")


# Printando o resultado final
print("----Comparação entre os tempos----")
for i in range(len(results_insert)):
    nome = results_insert[i][0]
    tempo_insert = results_insert[i][1]
    tempo_select = results_selection[i][1]
    print(f"{nome}: Insertion = {tempo_insert:.4f}segundos | Selection = {tempo_select:.4f}segundos")

    if tempo_insert > tempo_select:
        print(f"O select é melhor por {(tempo_insert - tempo_select):.4f}segundos")
    else:
        print(f"O insert é melhor por {(tempo_select - tempo_insert):.4f}segundos")
