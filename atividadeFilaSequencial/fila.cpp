#include "Fila.h"

Fila::Fila(int capacidade) {
    this->capacidade = capacidade;
    dados = new int[capacidade];
    inicio = 0;
    fim = -1;
    qtd = 0;
}

Fila::~Fila() {
    delete[] dados;
}

bool Fila::inserir(int valor) {
    if (estaCheia()) return false;
    fim = (fim + 1) % capacidade; // incremento circular
    dados[fim] = valor;
    qtd++;
    return true;
}

bool Fila::remover(int &valor) {
    if (estaVazia()) return false;
    valor = dados[inicio];
    inicio = (inicio + 1) % capacidade; // incremento circular
    qtd--;
    return true;
}

bool Fila::consultarInicio(int &valor) const {
    if (estaVazia()) return false;
    valor = dados[inicio];
    return true;
}

bool Fila::estaVazia() const {
    return qtd == 0;
}

bool Fila::estaCheia() const {
    return qtd == capacidade;
}

void Fila::imprimir() const {
    cout << "Fila: ";
    for (int i = 0; i < qtd; i++) {
        int idx = (inicio + i) % capacidade;
        cout << dados[idx] << " ";
    }
    cout << endl;
}
