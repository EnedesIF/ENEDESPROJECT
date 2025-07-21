#!/bin/bash

# ========================================
# Script de Setup Automático - Sistema ENEDES
# ========================================

echo "🚀 Iniciando setup do Sistema ENEDES..."
echo "========================================"

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.8 ou superior."
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Por favor, instale pip."
    exit 1
fi

echo "✅ pip encontrado: $(pip3 --version)"

# Navegar para o diretório do backend
cd enedes-backend || {
    echo "❌ Diretório enedes-backend não encontrado!"
    exit 1
}

echo "📁 Navegando para enedes-backend..."

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo "✅ Ambiente virtual criado com sucesso!"
    else
        echo "❌ Erro ao criar ambiente virtual!"
        exit 1
    fi
else
    echo "✅ Ambiente virtual já existe!"
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Atualizar pip
echo "🔧 Atualizando pip..."
pip install --upgrade pip

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependências instaladas com sucesso!"
else
    echo "❌ Erro ao instalar dependências!"
    exit 1
fi

# Verificar se arquivo .env existe
if [ ! -f ".env" ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "📝 Criando arquivo .env de exemplo..."
    
    cat > .env << EOL
# Configurações do Banco de Dados Neon PostgreSQL
DATABASE_URL=postgresql://neondb_owner:npg_IdLoQ18TaPAn@ep-holy-dawn-aexetnsr-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require

# Configurações da aplicação
SECRET_KEY=enedes_secret_key_2024
FLASK_ENV=development
CORS_ORIGINS=*
PORT=5000
EOL
    
    echo "✅ Arquivo .env criado! Verifique as configurações antes de continuar."
else
    echo "✅ Arquivo .env encontrado!"
fi

# Testar conexão com banco de dados
echo "🔍 Testando conexão com banco de dados..."
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()

try:
    import psycopg2
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    conn.close()
    print('✅ Conexão com banco de dados bem-sucedida!')
except Exception as e:
    print(f'❌ Erro na conexão com banco de dados: {e}')
    print('⚠️  Verifique as credenciais no arquivo .env')
"

echo ""
echo "🎉 Setup concluído!"
echo "========================================"
echo ""
echo "📋 Próximos passos:"
echo "1. Verifique as configurações no arquivo .env"
echo "2. Execute: python src/main.py"
echo "3. Acesse: http://localhost:5000"
echo ""
echo "📚 Para mais informações, consulte:"
echo "   - README.md"
echo "   - GUIA_COMPLETO_SETUP.md"
echo ""
echo "🚀 Para deploy no Vercel:"
echo "1. npm install -g vercel"
echo "2. vercel login"
echo "3. vercel --prod"
echo ""
echo "✨ Sistema ENEDES pronto para uso!"

