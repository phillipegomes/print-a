#!/bin/bash

echo "🚨 INICIANDO PROCEDIMENTO SUPREMO PARA RESETAR GIT LIMPO E EMPURRAR SEM ARQUIVOS PESADOS..."

# Caminhos
BACKUP_DIR="../print-a-backup-$(date +%Y%m%d_%H%M%S)"
CLONE_DIR="../print-a-clean"

echo "📦 1. Fazendo backup completo do projeto atual em $BACKUP_DIR"
cp -R ./ "$BACKUP_DIR"

echo "🌱 2. Clonando repositório limpo do GitHub"
git clone https://github.com/phillipegomes/print-a.git "$CLONE_DIR"

echo "🧹 3. Limpando repositório clonado e preparando nova base"
cd "$CLONE_DIR"
rm -rf .git

echo "📁 4. Copiando arquivos do projeto original para o clone limpo"
cp -R "$BACKUP_DIR"/* .

echo "📝 5. Criando .gitignore com boas práticas"
cat <<EOF > .gitignore
# Imagens e vídeos
*.jpg
*.jpeg
*.png
*.gif
*.mp4
*.mov
*.zip

# Diretórios e arquivos temporários
eventos_backup/
logs/
__pycache__/
*.pyc
*.log
*.save
*.txt
*.DS_Store
EOF

echo "🌐 6. Inicializando novo repositório Git"
git init
git remote add origin https://github.com/phillipegomes/print-a.git
git add .
git commit -m '🧼 Repositório limpo com .gitignore e sem arquivos pesados'

echo "✂️ 7. Removendo históricos de blobs grandes (>50MB)"
git filter-repo --force --strip-blobs-bigger-than 50M

echo "🚀 8. Subindo com força total (push --force)"
git push origin main --force

echo "✅ Processo concluído com sucesso! Seu repositório agora está limpo, leve e sem arquivos desnecessários."
