#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100 // Definindo o tamanho m�ximo da lista

typedef struct {
    int data[MAX_SIZE];
    int size;
} Lista;

// Cria a lista vazia
void criarLista(Lista* lista) {
    lista->size = 0;
}

// Verifica se a lista est� vazia
int listaVazia(Lista* lista) {
    return lista->size == 0;
}

// Verifica se a lista est� cheia
int listaCheia(Lista* lista) {
    return lista->size == MAX_SIZE;
}

// Obtem o tamanho da lista
int tamanhoLista(Lista* lista) {
    return lista->size;
}

// Obtem o valor de um elemento na lista
int obterElemento(Lista* lista, int posicao) {
    if (posicao < 1 || posicao > lista->size) {
        printf("Posicao invalida!\n");
        return -1; // Retorna -1 em caso de erro
    }
    return lista->data[posicao - 1];
}

// Modifica o elemento em uma posicao especifica
void modificarElemento(Lista* lista, int posicao, int valor) {
    if (posicao < 1 || posicao > lista->size) {
        printf("Posicao invalida!\n");
        return;
    }
    lista->data[posicao - 1] = valor;
}

// Insere um elemento em uma posicao especifica
void inserirElemento(Lista* lista, int posicao, int valor) {
    if (listaCheia(lista)) {
        printf("Lista cheia!\n");
        return;
    }
    if (posicao < 1 || posicao > lista->size + 1) {
        printf("Posicao invalida!\n");
        return;
    }
    for (int i = lista->size; i >= posicao; i--) {
        lista->data[i] = lista->data[i - 1];
    }
    lista->data[posicao - 1] = valor;
    lista->size++;
}

// Retirar um elemento de uma posicao especifica
void retirarElemento(Lista* lista, int posicao) {
    if (posicao < 1 || posicao > lista->size) {
        printf("Posicao invalida!\n");
        return;
    }
    for (int i = posicao - 1; i < lista->size - 1; i++) {
        lista->data[i] = lista->data[i + 1];
    }
    lista->size--;
}

// Imprime a lista
void imprimirLista(Lista* lista) {
    if (listaVazia(lista)) {
        printf("Lista vazia.\n");
        return;
    }
    for (int i = 0; i < lista->size; i++) {
        printf("%d ", lista->data[i]);
    }
    printf("\n");
}

int main() {
    Lista lista;
    criarLista(&lista);

    // Testando as fun��es
    inserirElemento(&lista, 1, 10);
    inserirElemento(&lista, 2, 20);
    inserirElemento(&lista, 3, 30);

    printf("Lista apos insercoess: ");
    imprimirLista(&lista);

    printf("Elemento na posicao 2: %d\n", obterElemento(&lista, 2));

    modificarElemento(&lista, 2, 25);
    printf("Lista apos modificacao na posicao 2: ");
    imprimirLista(&lista);

    retirarElemento(&lista, 3);
    printf("Lista apos retirar elemento na posicao 3: ");
    imprimirLista(&lista);

    return 0;
}
