#ifndef FILA_H
#define FILA_H

#include <iostream>
using namespace std;

class Fila {
private:
    int *dados;     // vetor de inteiros
    int capacidade; // tamanho máximo
    int inicio;     // índice do primeiro elemento
    int fim;        // índice do último elemento
    int qtd;        // quantidade de elementos

public:
    Fila(int capacidade);
    ~Fila();

    bool inserir(int valor); // inserir no fim
    bool remover(int &valor); // remover do início
    bool consultarInicio(int &valor) const; // ler o início sem remover
    bool estaVazia() const;
    bool estaCheia() const;
    void imprimir() const; // opcional para debug
};

#endif
