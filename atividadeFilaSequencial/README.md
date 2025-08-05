
Implementa��o de uma **fila de inteiros** utilizando **vetor est�tico** e **incremento circular**.

Este projeto foi desenvolvido para a disciplina de **Estrutura de Dados**, com as seguintes funcionalidades:

- Inserir no fim da fila  
- Remover do in�cio da fila  
- Consultar o in�cio da fila  
- Indicar se a fila est� vazia  
- Indicar se a fila est� cheia  

---

## ?? Estrutura de Arquivos

FilaCircular/  
??? Fila.h       # Defini��o da classe Fila  
??? Fila.cpp     # Implementa��o da classe Fila  
??? main.cpp     # Programa principal para testes  
??? Makefile     # Compila��o automatizada (Linux/Mac ou Windows com make)  
??? README.md    # Este arquivo  

---

## ?? Como Compilar e Executar

### **Op��o 1 � Usando g++ diretamente**

#### Windows (PowerShell ou CMD)  
g++ main.cpp Fila.cpp -o main.exe  
.\main.exe  

#### Linux / WSL  
g++ main.cpp Fila.cpp -o main  
./main  

---

### **Op��o 2 � Usando make**

Se voc� j� tiver o **make** instalado no seu sistema:

#### Linux / WSL  
make  
./main  

#### Windows  
make  
.\main.exe  

---

### **Para limpar arquivos compilados**
make clean
