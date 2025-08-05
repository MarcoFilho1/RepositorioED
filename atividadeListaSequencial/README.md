
Implementação de uma **fila de inteiros** utilizando **vetor estático** e **incremento circular**.

Este projeto foi desenvolvido para a disciplina de **Estrutura de Dados**, com as seguintes funcionalidades:

- Inserir no fim da fila  
- Remover do início da fila  
- Consultar o início da fila  
- Indicar se a fila está vazia  
- Indicar se a fila está cheia  

---

## ?? Estrutura de Arquivos

FilaCircular/  
??? Fila.h       # Definição da classe Fila  
??? Fila.cpp     # Implementação da classe Fila  
??? main.cpp     # Programa principal para testes  
??? Makefile     # Compilação automatizada (Linux/Mac ou Windows com make)  
??? README.md    # Este arquivo  

---

## ?? Como Compilar e Executar

### **Opção 1 — Usando g++ diretamente**

#### Windows (PowerShell ou CMD)  
g++ main.cpp Fila.cpp -o main.exe  
.\main.exe  

#### Linux / WSL  
g++ main.cpp Fila.cpp -o main  
./main  

---

### **Opção 2 — Usando make**

Se você já tiver o **make** instalado no seu sistema:

#### Linux / WSL  
make  
./main  

#### Windows  
make  
.\main.exe  

---

### **Para limpar arquivos compilados**
make clean
