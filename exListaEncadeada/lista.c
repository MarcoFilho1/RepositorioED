#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

typedef struct Node {
    int valor;
    struct Node* prox;
} Node;

typedef struct {
    Node* inicio;
    int tamanho;
} Lista;

Lista* criar_lista() {
    Lista* lista = (Lista*)malloc(sizeof(Lista));
    lista->inicio = NULL;
    lista->tamanho = 0;
    return lista;
}

int lista_vazia(Lista* lista) {
    return (lista->tamanho == 0);
}

int tamanho_lista(Lista* lista) {
    return lista->tamanho;
}

//obtem o valor em uma posicao
int obter_elemento(Lista* lista, int pos, int* valor){
    if(pos < 1 || pos > lista->tamanho) 
        return 0;

    Node* atual = lista->inicio;
    for (int i=1; i<pos; i++)
        atual = atual->prox;

    *valor = atual->valor;
    return 1;

}

int modificar_elemento(Lista* lista, int pos, int novo_valor) {
    if(pos < 1 || pos > lista->tamanho) 
        return 0;

    Node* atual = lista->inicio;
    for (int i = 1; i < pos; i++)
        atual = atual->prox;

    atual->valor = novo_valor;
    return 1;

}

int inserir_elemento(Lista* lista, int pos, int valor){
    if (pos < 1 || pos > lista->tamanho + 1 )
        return 0;

    Node* novo = (Node*)malloc(sizeof(Node));
    novo->valor = valor;
    novo->prox = NULL;

    if (pos == 1) {
        novo->prox = lista->inicio;
        lista->inicio = novo;
    } else {
        Node* atual = lista->inicio;
        for(int i = 1; i < pos - 1; i++){
            atual = atual->prox;
        }

        novo->prox = atual->prox;
        atual->prox = novo;
    }

    lista->tamanho++;
    return 1;

}


int remover_elemento(Lista* lista, int pos) {
    if (pos < 1 || pos > lista->tamanho)
        return 0;
    
    Node* temp;
    
    if(pos == 1) {
        temp = lista->inicio;
        lista->inicio = temp->prox;
    } else {
        Node* atual = lista->inicio;
        for (int i = 1; i < pos; i++)
            atual = atual->prox;

        temp = atual->prox;
        atual->prox = temp->prox;
    }

    free(temp);
    lista->tamanho--;
    return 1;

}

void imprimir_lista(Lista* lista) {
    Node* atual = lista->inicio;
    int i = 1;
    while(atual){
        printf("[%d] %d -> ", i++, atual->valor);
        atual = atual->prox;
    }
    printf("NULL\n");
}

void liberar_lista(Lista* lista){
    Node* atual = lista->inicio;
    while(atual){
        Node* temp = atual;
        atual = atual->prox;
        free(temp);
    }
    free(lista);
}


#include <unistd.h>  // Adicione isso no topo junto com stdio.h e stdlib.h

int main() {
    Lista* list = criar_lista();

    printf(">>> Inserindo elementos iniciais...\n");
    inserir_elemento(list, 1, 10);
    inserir_elemento(list, 2, 20);
    inserir_elemento(list, 2, 15);
    imprimir_lista(list);
    Sleep(300);  

    int val;

    printf("\n>>> Obtendo elemento na posicao 2...\n");
    if (obter_elemento(list, 2, &val))
        printf("Elemento na posicao 2: %d\n", val);
    Sleep(500);

    printf("\n>>> Modificando valor da posicao 3 para 99...\n");
    modificar_elemento(list, 3, 99);
    imprimir_lista(list);
    Sleep(500);

    printf("\n>>> Removendo elemento da posicao 1...\n");
    remover_elemento(list, 1);
    imprimir_lista(list);
    Sleep(500);

    printf("\n>>> Inserindo 5 na posicao 1...\n");
    inserir_elemento(list, 1, 5);
    imprimir_lista(list);
    Sleep(500);

    printf("\n>>> Inserindo 100 na posicao 3...\n");
    inserir_elemento(list, 3, 100);
    imprimir_lista(list);
    Sleep(500);

    printf("\n>>> Removendo elemento da posicao 2...\n");
    remover_elemento(list, 2);
    imprimir_lista(list);
    Sleep(500);

    printf("\n>>> Modificando valor da posicao 1 para 42...\n");
    modificar_elemento(list, 1, 42);
    imprimir_lista(list);
    Sleep(500);

    printf("\n>>> Tamanho atual da lista: %d\n", tamanho_lista(list));
    printf(">>> A lista esta vazia? %s\n", lista_vazia(list) ? "Sim" : "Não");
    Sleep(300);

    liberar_lista(list);
    return 0;
}
