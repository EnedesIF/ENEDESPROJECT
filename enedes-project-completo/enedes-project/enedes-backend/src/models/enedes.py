from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Meta(db.Model):
    """Modelo para Metas Estratégicas"""
    __tablename__ = 'metas'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # Campo em inglês para compatibilidade com frontend
    objetivo = db.Column(db.Text)
    program = db.Column(db.String(100), nullable=False)  # Campo em inglês para compatibilidade
    indicadores = db.Column(db.Text)  # JSON string com array de indicadores
    status = db.Column(db.String(50), default='ativo')
    created_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'titulo': self.title,  # Compatibilidade com frontend
            'objetivo': self.objetivo,
            'program': self.program,
            'programa': self.program,  # Compatibilidade com frontend
            'indicadores': json.loads(self.indicadores) if self.indicadores else [],
            'status': self.status,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Action(db.Model):
    """Modelo para Ações"""
    __tablename__ = 'actions'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # Campo em inglês
    titulo = db.Column(db.String(255), nullable=False)  # Campo em português para compatibilidade
    programa = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    responsavel = db.Column(db.String(100))
    status = db.Column(db.String(50), default='pending')  # pending, in_progress, completed
    created_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'titulo': self.titulo,
            'programa': self.programa,
            'descricao': self.descricao,
            'responsavel': self.responsavel,
            'status': self.status,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class FollowUp(db.Model):
    """Modelo para Follow-ups"""
    __tablename__ = 'followups'
    
    id = db.Column(db.Integer, primary_key=True)
    target_id = db.Column(db.Integer, nullable=False)  # ID da meta ou ação
    type = db.Column(db.String(20), nullable=False)  # 'action' ou 'meta'
    mensagem = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), default='media')  # baixa, media, alta, urgente
    prazo = db.Column(db.Date)
    colaboradores = db.Column(db.Text)  # JSON string com array de colaboradores
    status = db.Column(db.String(50), default='pending')  # pending, in_progress, completed
    observations = db.Column(db.Text)  # JSON string com observações
    created_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'target_id': self.target_id,
            'type': self.type,
            'mensagem': self.mensagem,
            'prioridade': self.prioridade,
            'prazo': self.prazo.isoformat() if self.prazo else None,
            'colaboradores': json.loads(self.colaboradores) if self.colaboradores else [],
            'status': self.status,
            'observations': json.loads(self.observations) if self.observations else [],
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Task(db.Model):
    """Modelo para Tarefas"""
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    followup_id = db.Column(db.Integer, db.ForeignKey('followups.id'), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    responsavel = db.Column(db.String(100))
    status = db.Column(db.String(50), default='pending')  # pending, in_progress, completed
    prazo = db.Column(db.Date)
    attachments = db.Column(db.Text)  # JSON string com anexos
    comments = db.Column(db.Text)  # JSON string com comentários
    created_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamento
    followup = db.relationship('FollowUp', backref=db.backref('tasks', lazy=True))
    
    def to_dict(self):
        return {
            'id': self.id,
            'followup_id': self.followup_id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'responsavel': self.responsavel,
            'status': self.status,
            'prazo': self.prazo.isoformat() if self.prazo else None,
            'attachments': json.loads(self.attachments) if self.attachments else [],
            'comments': json.loads(self.comments) if self.comments else [],
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Cronograma(db.Model):
    """Modelo para Cronograma"""
    __tablename__ = 'cronograma'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    inicio = db.Column(db.Date)
    fim = db.Column(db.Date)
    rubrica = db.Column(db.Numeric(12, 2), default=0)  # Valor orçado
    executado = db.Column(db.Numeric(12, 2), default=0)  # Valor executado
    created_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'inicio': self.inicio.isoformat() if self.inicio else None,
            'fim': self.fim.isoformat() if self.fim else None,
            'rubrica': float(self.rubrica) if self.rubrica else 0,
            'executado': float(self.executado) if self.executado else 0,
            'saldo': float(self.rubrica - self.executado) if self.rubrica and self.executado else 0,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Inventario(db.Model):
    """Modelo para Inventário"""
    __tablename__ = 'inventario'
    
    id = db.Column(db.Integer, primary_key=True)
    programa = db.Column(db.String(100), nullable=False)
    item = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    valor = db.Column(db.Numeric(12, 2), default=0)
    atividades_relacionadas = db.Column(db.String(255))
    created_by = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'programa': self.programa,
            'item': self.item,
            'descricao': self.descricao,
            'valor': float(self.valor) if self.valor else 0,
            'atividades_relacionadas': self.atividades_relacionadas,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class ActivityLog(db.Model):
    """Modelo para Log de Atividades"""
    __tablename__ = 'activity_log'
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(20), default='info')  # info, success, warning, error
    icon = db.Column(db.String(50))
    user = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'type': self.type,
            'icon': self.icon,
            'user': self.user,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

