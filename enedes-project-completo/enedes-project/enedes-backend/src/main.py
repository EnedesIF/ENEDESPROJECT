import os
import sys
from dotenv import load_dotenv

# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Carregar variáveis de ambiente
load_dotenv()

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.enedes import db
from src.routes.enedes import enedes_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configurações de segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'enedes_secret_key_2024')

# Configuração CORS para permitir acesso do frontend
CORS(app, origins=os.getenv('CORS_ORIGINS', '*').split(','))

# Registrar blueprints da API
app.register_blueprint(enedes_bp, url_prefix='/api')

# Configuração do banco PostgreSQL Neon
database_url = os.getenv('DATABASE_URL')
if database_url:
    # Ajustar URL para SQLAlchemy se necessário
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Fallback para configuração manual
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', 5432)}/{os.getenv('DB_NAME')}"
        f"?sslmode=require"
    )

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}

# Inicializar banco de dados
db.init_app(app)

# Criar tabelas se não existirem
with app.app_context():
    try:
        db.create_all()
        print("✅ Tabelas do banco de dados criadas/verificadas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {e}")

# Rota para servir o frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

# Rota de health check
@app.route('/health')
def health_check():
    return {
        'status': 'healthy',
        'database': 'connected',
        'environment': os.getenv('FLASK_ENV', 'development')
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)

