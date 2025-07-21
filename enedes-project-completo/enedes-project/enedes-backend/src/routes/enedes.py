from flask import Blueprint, request, jsonify
from src.models.enedes import db, Meta, Action, FollowUp, Task, Cronograma, Inventario, ActivityLog
from datetime import datetime
import json

enedes_bp = Blueprint('enedes', __name__)

# ========================================
# ENDPOINT DE TESTE
# ========================================
@enedes_bp.route('/test', methods=['GET'])
def test_connection():
    """Endpoint para testar conectividade"""
    return jsonify({
        'success': True,
        'message': 'API ENEDES funcionando!',
        'timestamp': datetime.utcnow().isoformat(),
        'endpoints': ['test', 'goals', 'actions', 'followups', 'tasks', 'schedule', 'inventory', 'activity-log']
    })

# ========================================
# METAS (GOALS)
# ========================================
@enedes_bp.route('/goals', methods=['GET'])
def get_goals():
    """Listar todas as metas"""
    try:
        metas = Meta.query.all()
        return jsonify({
            'success': True,
            'data': [meta.to_dict() for meta in metas]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/goals', methods=['POST'])
def create_goal():
    """Criar nova meta"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data.get('title'):
            return jsonify({'success': False, 'error': 'Título é obrigatório'}), 400
        
        # Processar indicadores
        indicadores = data.get('indicadores', [])
        if isinstance(indicadores, list):
            indicadores_json = json.dumps(indicadores)
        else:
            indicadores_json = json.dumps([])
        
        meta = Meta(
            title=data['title'],
            objetivo=data.get('objetivo', ''),
            program=data.get('program', ''),
            indicadores=indicadores_json,
            status=data.get('status', 'ativo'),
            created_by=data.get('created_by', 'Sistema')
        )
        
        db.session.add(meta)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': meta.id,
            'data': meta.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/goals', methods=['PUT'])
def update_goal():
    """Atualizar meta existente"""
    try:
        data = request.get_json()
        meta_id = data.get('id')
        
        if not meta_id:
            return jsonify({'success': False, 'error': 'ID é obrigatório'}), 400
        
        meta = Meta.query.get(meta_id)
        if not meta:
            return jsonify({'success': False, 'error': 'Meta não encontrada'}), 404
        
        # Atualizar campos
        if 'title' in data:
            meta.title = data['title']
        if 'objetivo' in data:
            meta.objetivo = data['objetivo']
        if 'program' in data:
            meta.program = data['program']
        if 'indicadores' in data:
            indicadores = data['indicadores']
            if isinstance(indicadores, list):
                meta.indicadores = json.dumps(indicadores)
        if 'status' in data:
            meta.status = data['status']
        
        meta.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': meta.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/goals', methods=['DELETE'])
def delete_goal():
    """Excluir meta"""
    try:
        data = request.get_json()
        meta_id = data.get('id')
        
        if not meta_id:
            return jsonify({'success': False, 'error': 'ID é obrigatório'}), 400
        
        meta = Meta.query.get(meta_id)
        if not meta:
            return jsonify({'success': False, 'error': 'Meta não encontrada'}), 404
        
        db.session.delete(meta)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': meta.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ========================================
# AÇÕES (ACTIONS)
# ========================================
@enedes_bp.route('/actions', methods=['GET'])
def get_actions():
    """Listar todas as ações"""
    try:
        actions = Action.query.all()
        return jsonify({
            'success': True,
            'data': [action.to_dict() for action in actions]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/actions', methods=['POST'])
def create_action():
    """Criar nova ação"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data.get('titulo'):
            return jsonify({'success': False, 'error': 'Título é obrigatório'}), 400
        
        action = Action(
            title=data['titulo'],  # Usar titulo como title também
            titulo=data['titulo'],
            programa=data.get('programa', ''),
            descricao=data.get('descricao', ''),
            responsavel=data.get('responsavel', ''),
            status=data.get('status', 'pending'),
            created_by=data.get('created_by', 'Sistema')
        )
        
        db.session.add(action)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': action.id,
            'data': action.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/actions', methods=['PUT'])
def update_action():
    """Atualizar ação existente"""
    try:
        data = request.get_json()
        action_id = data.get('id')
        
        if not action_id:
            return jsonify({'success': False, 'error': 'ID é obrigatório'}), 400
        
        action = Action.query.get(action_id)
        if not action:
            return jsonify({'success': False, 'error': 'Ação não encontrada'}), 404
        
        # Atualizar campos
        if 'titulo' in data:
            action.titulo = data['titulo']
            action.title = data['titulo']  # Manter sincronizado
        if 'programa' in data:
            action.programa = data['programa']
        if 'descricao' in data:
            action.descricao = data['descricao']
        if 'responsavel' in data:
            action.responsavel = data['responsavel']
        if 'status' in data:
            action.status = data['status']
        
        action.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': action.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/actions', methods=['DELETE'])
def delete_action():
    """Excluir ação"""
    try:
        data = request.get_json()
        action_id = data.get('id')
        
        if not action_id:
            return jsonify({'success': False, 'error': 'ID é obrigatório'}), 400
        
        action = Action.query.get(action_id)
        if not action:
            return jsonify({'success': False, 'error': 'Ação não encontrada'}), 404
        
        db.session.delete(action)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'data': action.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ========================================
# FOLLOW-UPS
# ========================================
@enedes_bp.route('/followups', methods=['GET'])
def get_followups():
    """Listar todos os follow-ups"""
    try:
        followups = FollowUp.query.all()
        return jsonify({
            'success': True,
            'data': [followup.to_dict() for followup in followups]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/followups', methods=['POST'])
def create_followup():
    """Criar novo follow-up"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data.get('target_id') or not data.get('mensagem'):
            return jsonify({'success': False, 'error': 'Target ID e mensagem são obrigatórios'}), 400
        
        # Processar colaboradores
        colaboradores = data.get('colaboradores', [])
        if isinstance(colaboradores, (list, str)):
            colaboradores_json = json.dumps(colaboradores) if isinstance(colaboradores, list) else colaboradores
        else:
            colaboradores_json = json.dumps([])
        
        followup = FollowUp(
            target_id=data['target_id'],
            type=data.get('type', 'action'),
            mensagem=data['mensagem'],
            prioridade=data.get('prioridade', 'media'),
            prazo=datetime.strptime(data['prazo'], '%Y-%m-%d').date() if data.get('prazo') else None,
            colaboradores=colaboradores_json,
            status=data.get('status', 'pending'),
            created_by=data.get('created_by', 'Sistema')
        )
        
        db.session.add(followup)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': followup.id,
            'data': followup.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ========================================
# TAREFAS (TASKS)
# ========================================
@enedes_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Listar todas as tarefas"""
    try:
        tasks = Task.query.all()
        return jsonify({
            'success': True,
            'data': [task.to_dict() for task in tasks]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/tasks', methods=['POST'])
def create_task():
    """Criar nova tarefa"""
    try:
        data = request.get_json()
        
        # Validação básica
        if not data.get('followup_id') or not data.get('titulo'):
            return jsonify({'success': False, 'error': 'Follow-up ID e título são obrigatórios'}), 400
        
        # Processar anexos
        attachments = data.get('attachments', [])
        if isinstance(attachments, (list, str)):
            attachments_json = json.dumps(attachments) if isinstance(attachments, list) else attachments
        else:
            attachments_json = json.dumps([])
        
        task = Task(
            followup_id=data['followup_id'],
            titulo=data['titulo'],
            descricao=data.get('descricao', ''),
            responsavel=data.get('responsavel', ''),
            status=data.get('status', 'pending'),
            prazo=datetime.strptime(data['prazo'], '%Y-%m-%d').date() if data.get('prazo') else None,
            attachments=attachments_json,
            created_by=data.get('created_by', 'Sistema')
        )
        
        db.session.add(task)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': task.id,
            'data': task.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ========================================
# CRONOGRAMA (SCHEDULE)
# ========================================
@enedes_bp.route('/schedule', methods=['GET'])
def get_schedule():
    """Listar cronograma"""
    try:
        cronograma = Cronograma.query.all()
        return jsonify({
            'success': True,
            'data': [item.to_dict() for item in cronograma]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/schedule', methods=['POST'])
def create_schedule_item():
    """Criar item do cronograma"""
    try:
        data = request.get_json()
        
        if not data.get('nome'):
            return jsonify({'success': False, 'error': 'Nome é obrigatório'}), 400
        
        cronograma_item = Cronograma(
            nome=data['nome'],
            inicio=datetime.strptime(data['inicio'], '%Y-%m-%d').date() if data.get('inicio') else None,
            fim=datetime.strptime(data['fim'], '%Y-%m-%d').date() if data.get('fim') else None,
            rubrica=data.get('rubrica', 0),
            executado=data.get('executado', 0),
            created_by=data.get('created_by', 'Sistema')
        )
        
        db.session.add(cronograma_item)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': cronograma_item.id,
            'data': cronograma_item.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ========================================
# INVENTÁRIO (INVENTORY)
# ========================================
@enedes_bp.route('/inventory', methods=['GET'])
def get_inventory():
    """Listar inventário"""
    try:
        inventario = Inventario.query.all()
        return jsonify({
            'success': True,
            'data': [item.to_dict() for item in inventario]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/inventory', methods=['POST'])
def create_inventory_item():
    """Criar item do inventário"""
    try:
        data = request.get_json()
        
        if not data.get('item'):
            return jsonify({'success': False, 'error': 'Nome do item é obrigatório'}), 400
        
        inventario_item = Inventario(
            programa=data.get('programa', ''),
            item=data['item'],
            descricao=data.get('descricao', ''),
            valor=data.get('valor', 0),
            atividades_relacionadas=data.get('atividades_relacionadas', ''),
            created_by=data.get('created_by', 'Sistema')
        )
        
        db.session.add(inventario_item)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': inventario_item.id,
            'data': inventario_item.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# ========================================
# LOG DE ATIVIDADES
# ========================================
@enedes_bp.route('/activity-log', methods=['GET'])
def get_activity_log():
    """Listar log de atividades"""
    try:
        logs = ActivityLog.query.order_by(ActivityLog.timestamp.desc()).limit(100).all()
        return jsonify({
            'success': True,
            'data': [log.to_dict() for log in logs]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@enedes_bp.route('/activity-log', methods=['POST'])
def create_activity_log():
    """Criar entrada no log de atividades"""
    try:
        data = request.get_json()
        
        if not data.get('message'):
            return jsonify({'success': False, 'error': 'Mensagem é obrigatória'}), 400
        
        log_entry = ActivityLog(
            message=data['message'],
            type=data.get('type', 'info'),
            icon=data.get('icon', ''),
            user=data.get('user', 'Sistema')
        )
        
        db.session.add(log_entry)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'id': log_entry.id,
            'data': log_entry.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

