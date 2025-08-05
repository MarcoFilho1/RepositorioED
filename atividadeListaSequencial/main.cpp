#include "Fila.h"
#include <iostream>
using namespace std;

int main() {
    Fila fila(5);
    int valor;

    // Teste: inserir elementos
    cout << "Inserindo elementos..." << endl;
    for (int i = 1; i <= 5; i++) {
        if (fila.inserir(i * 10))
            cout << "Inserido: " << i * 10 << endl;
        else
            cout << "Fila cheia ao tentar inserir " << i * 10 << endl;
    }
    fila.imprimir();

    // Teste: consultar início
    if (fila.consultarInicio(valor))
        cout << "Inicio da fila: " << valor << endl;

    // Teste: remover dois elementos
    cout << "Removendo dois elementos..." << endl;
    for (int i = 0; i < 2; i++) {
        if (fila.remover(valor))
            cout << "Removido: " << valor << endl;
    }
    fila.imprimir();

    // Teste: inserir novamente (incremento circular)
    cout << "Inserindo mais elementos..." << endl;
    for (int i = 6; i <= 7; i++) {
        if (fila.inserir(i * 10))
            cout << "Inserido: " << i * 10 << endl;
        else
            cout << "Fila cheia ao tentar inserir " << i * 10 << endl;
    }
    fila.imprimir();

    // Teste: esvaziar fila
    cout << "Esvaziando fila..." << endl;
    while (!fila.estaVazia()) {
        fila.remover(valor);
        cout << "Removido: " << valor << endl;
    }
    fila.imprimir();

    return 0;
}
