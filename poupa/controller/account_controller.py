# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


from poupa.model.validators import AccountValidator, AccountTypeValidator
from poupa.model.account import Account, AccountType

from poupa.controller.context_manager import get_session

class AccountController():

    def create_account(self, account_data):
        validated_data = AccountValidator(**account_data).for_creation()
        with get_session() as session:
            account = Account(**validated_data)
            session.add(account)
            session.commit()

    def get_account(self, account_id):
        with get_session() as session:
            return session.query(Account).filter_by(id=account_id).first()
        
    def get_accounts_by_budget_id(self, budget_id):
        with get_session() as session:
            return session.query(Account).filter_by(budget_id=budget_id).all()    

    def update_account(self, account_id, updated_data):
        validated_data = AccountValidator(**updated_data).for_update()
        updated_data = {k: v for k, v in validated_data.items() if v is not None}
        with get_session() as session:
            account = session.query(Account).filter_by(id=account_id).first()
            if account:
                for key, value in updated_data.items():
                    setattr(account, key, value)
                session.commit()

    def delete_account(self, account_id):
        with get_session() as session:
            account = session.query(Account).filter_by(id=account_id).first()
            if account:
                session.delete(account)
                session.commit()

class AccountTypeController():
    def create_account_type(self, account_type_data):
        validated_data = AccountTypeValidator(**account_type_data).for_creation()
        with get_session() as session:
            account_type = AccountType(**validated_data)
            session.add(account_type)
            session.commit()

    def get_account_type_by_id(self, account_type_id):
        with get_session() as session:
            return session.query(AccountType).filter_by(id=account_type_id).first()
    
    def update_account_type(self, account_type_id, updated_data):
        with get_session() as session:
            validated_data = AccountTypeValidator(**updated_data).for_update()
            updated_data = {k: v for k, v in validated_data.items() if v is not None}
            account_type = session.query(AccountType).filter_by(id=account_type_id).first()
            if account_type:
                for key, value in updated_data.items():
                    setattr(account_type, key, value)
                session.commit()

    def delete_account_type(self, account_type_id):
        with get_session() as session:
            account_type = session.query(AccountType).filter_by(id=account_type_id).first()
            if account_type:
                session.delete(account_type)
                session.commit()