# Compilando o código C diretamente com o GCC
echo "Compilando o codigo com GCC..."
gcc -Wall main.c -o lista

# Verifica se a compilação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "Compilacao bem-sucedida!"
else
    echo "Erro na compilacao."
fi

# Pausa para visualizar a saída
echo "Pressione qualquer tecla para continuar..."
read -n 1