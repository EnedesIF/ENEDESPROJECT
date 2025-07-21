# 🚀 Início Rápido - Sistema ENEDES

## ⚡ Setup Automático (Recomendado)

```bash
# 1. Clone o repositório
git clone <seu-repositorio>
cd enedes-project

# 2. Execute o script de setup
./setup.sh

# 3. Inicie a aplicação
cd enedes-backend
source venv/bin/activate
python src/main.py
```

## 📱 Acesso

- **Local**: http://localhost:5000
- **API Test**: http://localhost:5000/api/test

## 🌐 Deploy Rápido no Vercel

```bash
# 1. Instalar Vercel CLI
npm install -g vercel

# 2. Login
vercel login

# 3. Deploy (na pasta enedes-backend)
cd enedes-backend
vercel --prod
```

## 🔧 Configuração Manual

Se preferir configurar manualmente:

### 1. Ambiente Virtual
```bash
cd enedes-backend
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
```

### 2. Dependências
```bash
pip install -r requirements.txt
```

### 3. Variáveis de Ambiente
Crie `.env` na pasta `enedes-backend`:
```env
DATABASE_URL=postgresql://neondb_owner:npg_IdLoQ18TaPAn@ep-holy-dawn-aexetnsr-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require
SECRET_KEY=enedes_secret_key_2024
FLASK_ENV=development
CORS_ORIGINS=*
```

### 4. Executar
```bash
python src/main.py
```

## 📊 Funcionalidades Disponíveis

- ✅ **Metas**: Gestão de objetivos estratégicos
- ✅ **Ações**: Controle de atividades
- ✅ **Follow-ups**: Acompanhamento contínuo
- ✅ **Tarefas**: Gerenciamento detalhado
- ✅ **Cronograma**: Planejamento temporal
- ✅ **Inventário**: Controle de recursos

## 🆘 Problemas Comuns

### Erro de Conexão com Banco
- Verifique credenciais no `.env`
- Teste conectividade: `ping ep-holy-dawn-aexetnsr-pooler.c-2.us-east-2.aws.neon.tech`

### Erro no Vercel
- Verifique variáveis de ambiente no dashboard
- Consulte logs de deploy

### API não responde
- Verifique se Flask está rodando
- Teste endpoint: `/api/test`

## 📚 Documentação Completa

Para instruções detalhadas, consulte:
- `GUIA_COMPLETO_SETUP.md` - Setup completo
- `README.md` - Documentação técnica

## 🔗 Links Úteis

- **Neon Console**: https://console.neon.tech
- **Vercel Dashboard**: https://vercel.com/dashboard
- **Flask Docs**: https://flask.palletsprojects.com

---

**Sistema ENEDES - Gestão Estratégica Moderna** 🎯

