echo "🚨 INICIANDO LIMPEZA DO PROJETO PRINT A..."

# Caminho base do seu projeto (ajuste se necessário)
PROJETO_PATH="$PWD"

# Confirma diretório
echo "📂 Projeto em: $PROJETO_PATH"

# Apaga todos os arquivos compilados .pyc
find "$PROJETO_PATH" -name "*.pyc" -exec rm -f {} \;

# Apaga todas as pastas __pycache__
find "$PROJETO_PATH" -type d -name "__pycache__" -exec rm -rf {} +

# Mostra arquivos remanescentes relacionados ao main_window
echo "📄 Arquivos contendo 'main_window.py':"
find "$PROJETO_PATH" -name "main_window.py"

# Mostra os 10 primeiros caracteres da linha 88 para validação final
echo "🔍 Verificando linha 88:"
sed -n '88p' "$PROJETO_PATH/src/ui/main_window.py" | cat -A

echo "✅ LIMPEZA FINALIZADA. Agora execute:"
echo "python3 main.py"
