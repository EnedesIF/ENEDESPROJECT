# Sistema ENEDES

Sistema de gestão estratégica com backend Flask e integração PostgreSQL Neon.

## 🚀 Tecnologias

- **Backend**: Flask (Python)
- **Banco de Dados**: PostgreSQL (Neon)
- **Frontend**: HTML/CSS/JavaScript
- **Deploy**: Vercel

## 📋 Funcionalidades

- ✅ Gestão de Metas Estratégicas
- ✅ Controle de Ações
- ✅ Sistema de Follow-ups
- ✅ Gerenciamento de Tarefas
- ✅ Cronograma de Atividades
- ✅ Inventário de Recursos
- ✅ Log de Atividades

## 🛠️ Configuração Local

### 1. Clonar o repositório
```bash
git clone <seu-repositorio>
cd enedes-backend
```

### 2. Configurar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=postgresql://neondb_owner:npg_IdLoQ18TaPAn@ep-holy-dawn-aexetnsr-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require
SECRET_KEY=enedes_secret_key_2024
FLASK_ENV=development
CORS_ORIGINS=*
```

### 5. Executar aplicação
```bash
python src/main.py
```

A aplicação estará disponível em: http://localhost:5000

## 🌐 Deploy no Vercel

### 1. Instalar Vercel CLI
```bash
npm install -g vercel
```

### 2. Fazer login no Vercel
```bash
vercel login
```

### 3. Configurar variáveis de ambiente no Vercel
No dashboard do Vercel, adicione as seguintes variáveis:
- `DATABASE_URL`: Sua string de conexão Neon
- `SECRET_KEY`: Chave secreta da aplicação
- `FLASK_ENV`: production

### 4. Deploy
```bash
vercel --prod
```

## 📊 API Endpoints

### Teste de Conectividade
- `GET /api/test` - Testar API

### Metas
- `GET /api/goals` - Listar metas
- `POST /api/goals` - Criar meta
- `PUT /api/goals` - Atualizar meta
- `DELETE /api/goals` - Excluir meta

### Ações
- `GET /api/actions` - Listar ações
- `POST /api/actions` - Criar ação
- `PUT /api/actions` - Atualizar ação
- `DELETE /api/actions` - Excluir ação

### Follow-ups
- `GET /api/followups` - Listar follow-ups
- `POST /api/followups` - Criar follow-up

### Tarefas
- `GET /api/tasks` - Listar tarefas
- `POST /api/tasks` - Criar tarefa

### Cronograma
- `GET /api/schedule` - Listar cronograma
- `POST /api/schedule` - Criar item do cronograma

### Inventário
- `GET /api/inventory` - Listar inventário
- `POST /api/inventory` - Criar item do inventário

### Log de Atividades
- `GET /api/activity-log` - Listar logs
- `POST /api/activity-log` - Criar log

## 🔧 Estrutura do Projeto

```
enedes-backend/
├── src/
│   ├── models/
│   │   └── enedes.py          # Modelos do banco de dados
│   ├── routes/
│   │   └── enedes.py          # Rotas da API
│   ├── static/
│   │   └── index.html         # Frontend
│   └── main.py                # Aplicação principal
├── .env                       # Variáveis de ambiente
├── .gitignore                 # Arquivos ignorados pelo Git
├── requirements.txt           # Dependências Python
├── vercel.json               # Configuração do Vercel
└── README.md                 # Este arquivo
```

## 🗄️ Banco de Dados

O sistema utiliza PostgreSQL hospedado no Neon. As tabelas são criadas automaticamente na primeira execução.

### Modelos de Dados:
- **Meta**: Metas estratégicas
- **Action**: Ações do sistema
- **FollowUp**: Follow-ups de metas/ações
- **Task**: Tarefas relacionadas aos follow-ups
- **Cronograma**: Cronograma de atividades
- **Inventario**: Inventário de recursos
- **ActivityLog**: Log de atividades do sistema

## 🔒 Segurança

- CORS configurado para permitir acesso do frontend
- Variáveis de ambiente para credenciais sensíveis
- Conexão SSL com o banco de dados
- Validação de dados nas APIs

## 📞 Suporte

Para dúvidas ou problemas, consulte a documentação ou entre em contato com a equipe de desenvolvimento.
# ENEDESPROJECT
