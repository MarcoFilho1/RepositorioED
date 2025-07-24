# Teste 1: Executa o programa e verifica se a saída contém a mensagem esperada
echo "Executando Teste 1: Insercao de elementos"
output=$(./lista)
echo "$output" | grep -q "Lista apos insercoes:"
if [ $? -eq 0 ]; then
    echo "Teste 1: Sucesso - Insercao de elementos."
else
    echo "Teste 1: Falha - Insercao de elementos."
fi

# Teste 2: Verificar a modificação de um elemento
echo "Executando Teste 2: Modificação de elementos"
output=$(./lista)
echo "$output" | grep -q "Lista apos modificacao na posicao 2:"
if [ $? -eq 0 ]; then
    echo "Teste 2: Sucesso - Modificacao de elementos."
else
    echo "Teste 2: Falha - Modificacao de elementos."
fi

# Teste 3: Verificar a retirada de um elemento
echo "Executando Teste 3: Retirada de elementos"
output=$(./lista)
echo "$output" | grep -q "Lista apos retirar elemento na posicao 3:"
if [ $? -eq 0 ]; then
    echo "Teste 3: Sucesso - Retirada de elementos."
else
    echo "Teste 3: Falha - Retirada de elementos."
fi

# Pausa para visualizar a saída
echo "Pressione qualquer tecla para continuar..."
read -n 1