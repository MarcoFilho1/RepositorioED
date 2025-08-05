#ifndef FILA_H
#define FILA_H

#include <iostream>
using namespace std;

class Fila {
private:
    int *dados;     // vetor de inteiros
    int capacidade; // tamanho m�ximo
    int inicio;     // �ndice do primeiro elemento
    int fim;        // �ndice do �ltimo elemento
    int qtd;        // quantidade de elementos

public:
    Fila(int capacidade);
    ~Fila();

    bool inserir(int valor); // inserir no fim
    bool remover(int &valor); // remover do in�cio
    bool consultarInicio(int &valor) const; // ler o in�cio sem remover
    bool estaVazia() const;
    bool estaCheia() const;
    void imprimir() const; // opcional para debug
};

#endif
