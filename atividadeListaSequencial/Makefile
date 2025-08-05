# Detecta o sistema operacional
ifeq ($(OS),Windows_NT)
    EXE = main.exe
    RM = del /Q
else
    EXE = main
    RM = rm -f
endif

CXX = g++
CXXFLAGS = -Wall -std=c++11

all: $(EXE)

$(EXE): main.o Fila.o
	$(CXX) $(CXXFLAGS) -o $(EXE) main.o Fila.o

main.o: main.cpp Fila.h
	$(CXX) $(CXXFLAGS) -c main.cpp

Fila.o: Fila.cpp Fila.h
	$(CXX) $(CXXFLAGS) -c Fila.cpp

clean:
	$(RM) *.o $(EXE)
