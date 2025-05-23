# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree

from typing import Optional, List

from poupa.model.budget import Budget
from poupa.model.validators import BudgetValidator

from poupa.controller.context_manager import get_session


class BudgetController:
        
    def create_budget(self, data: dict) -> Budget:
        """
        Cria um novo orçamento após validar os dados.
        :param data: Dicionário contendo os dados do orçamento.
        :return: Objeto Budget criado.
        """
        # Valida os dados do orçamento
        # O método model_dump() é usado para converter o modelo Pydantic em um dicionário        
        validated_data = BudgetValidator(**data).for_creation()
        
        with get_session() as session:
            budget = Budget(**validated_data)
            session.add(budget)
            session.commit()
            session.refresh(budget)
            return budget

    def get_all_budgets(self):
        """Retorna todos os orçamentos."""
        with get_session() as session:
            return session.query(Budget).all()

    def get_budget_by_id(self, budget_id: int):
        """
        Retorna um orçamento pelo ID.
        :param budget_id: ID do orçamento a ser buscado.
        :return: Objeto Budget se encontrado, ou None se não encontrado.
        """
        with get_session() as session:
            return session.query(Budget).filter(Budget.id == budget_id).first()
        
    def get_budget_by_name(self, name: str) -> List[Budget]:
        """
        Retorna uma lista de orçamentos que correspondem ao nome fornecido.
        :param name: Nome do orçamento.
        :return: Lista de orçamentos.
        """
        with get_session() as session:
            return session.query(Budget).filter(Budget.name.ilike(f"%{name}%")).all()

    def update_budget(self, budget_id: int, data: dict) -> Optional[Budget]:
        """
        Atualiza um orçamento existente após validar os dados.
        :param budget_id: ID do orçamento a ser atualizado.
        :param data: Dicionário contendo os dados atualizados.
        :return: Objeto Budget atualizado ou None se não encontrado.
        """
        with get_session() as session:
            budget = session.query(Budget).filter(Budget.id == budget_id).first()
            if not budget:
                return None

            # Mescla os dados existentes com os novos e valida
            updated_data = {**budget.__dict__, **data}
            validated_data = BudgetValidator(**updated_data).model_dump()

            # Atualiza os campos do orçamento
            for key, value in validated_data.items():
                setattr(budget, key, value)

            session.commit()
            session.refresh(budget)
            return budget

    def delete_budget(self, budget_id: int) -> bool:
        """
        Exclui um orçamento pelo ID.
        :param budget_id: ID do orçamento a ser excluído.
        :return: True se excluído com sucesso, False caso contrário.
        """
        with get_session() as session:
            budget = session.query(Budget).filter(Budget.id == budget_id).first()
            if budget:
                session.delete(budget)
                session.commit()
                return True
            return False
    