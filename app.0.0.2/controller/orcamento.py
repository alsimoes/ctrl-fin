from model.database import SessionLocal
from app.model.budget import Orcamento
import logging

logger = logging.getLogger()

def criar_orcamento(nome, moeda):
    """
    Cria um novo orçamento no banco de dados.

    Args:
        nome (str): Nome do orçamento.
        moeda (str): Moeda do orçamento.
        valor_total (float): Valor total do orçamento (opcional).

    Returns:
        Orcamento: O objeto do orçamento criado.
    """
    db = SessionLocal()
    try:
        novo_orcamento = Orcamento(nome=nome, moeda=moeda)
        db.add(novo_orcamento)
        db.commit()
        db.refresh(novo_orcamento)
        logger.info(f"Orçamento criado: {novo_orcamento}")
        return novo_orcamento
    except Exception as e:
        logger.error(f"Erro ao criar orçamento: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def listar_orcamentos():
    """
    Lista todos os orçamentos no banco de dados.

    Returns:
        list: Lista de objetos Orcamento.
    """
    db = SessionLocal()
    try:
        orcamentos = db.query(Orcamento).all()
        logger.info(f"{len(orcamentos)} orçamentos encontrados.")
        return orcamentos
    except Exception as e:
        logger.error(f"Erro ao listar orçamentos: {e}")
        raise
    finally:
        db.close()

def excluir_orcamento(orcamento_id):
    """
    Exclui um orçamento pelo ID.

    Args:
        orcamento_id (int): ID do orçamento a ser excluído.
    """
    db = SessionLocal()
    try:
        orcamento = db.query(Orcamento).filter(Orcamento.id == orcamento_id).first()
        if orcamento:
            db.delete(orcamento)
            db.commit()
            logger.info(f"Orçamento excluído: {orcamento}")
        else:
            logger.warning(f"Orçamento com ID {orcamento_id} não encontrado.")
    except Exception as e:
        logger.error(f"Erro ao excluir orçamento: {e}")
        db.rollback()
        raise
    finally:
        db.close()