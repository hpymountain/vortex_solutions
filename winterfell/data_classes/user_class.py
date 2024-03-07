from tokeo.ext.appshare import app
from winterfell.data_classes.database_object import DatabaseObject
from winterfell.data_classes.contract_class import Contract, get_all_contracts_in_db


class User(DatabaseObject):
    def __init__(self):
        self.ID: str = "" 
        self.forename: str = ""
        self.surname: str = ""
        self.address: str = ""
        self.zipcode: str = ""
        self.city: str = ""
        self.email: str = ""
        self.contracts: dict[str, Contract] = {}
    
    def read_from_query_object(self, query_object):
        self.ID = query_object.id
        self.forename = query_object.forename
        self.surname = query_object.surname
        self.address = query_object.address
        self.zipcode = query_object.zipcode
        self.city = query_object.city
        self.email = query_object.email
        
        self.fetch_all_contracts()
        return self
    
    def fetch_all_contracts(self):
        all_contracts = get_all_contracts_in_db()
        for id, contract in all_contracts.items():
            if contract.customer == self.ID:
                self.contracts.update({id: contract})
        return self
       
    def read_in_db(self, key:str):
        self.read_from_query_object(app.db.get_one('customers', key))
        return self
    
    def create_in_db(self):
        col_dict = {
            'id': self.ID,
            'forename': self.forename,
            'surname': self.surname,
            'address': self.address,
            'zipcode': self.zipcode,
            'city': self.city,
            'email': self.email
            }
        app.db.create('customers', col_dict)
        return self
    
    def update_in_db(self, col_list: list[str]=None):
        col_dict = {
            'forename': self.forename,
            'surname': self.surname,
            'address': self.address,
            'zipcode': self.zipcode,
            'city': self.city,
            'email': self.email
            }
        if col_list is not None:
            col_dict_new = dict(col_dict)
            for col in col_list:
                col_dict_new.update({col: col_dict.get(col)})
            col_dict = col_dict_new
        app.db.update('customers', self.ID, col_dict)
        return self
        
    def delete_in_db(self):
        app.db.delete('customers', self.ID)
        return self


def read_user_list_from_db(filter = None) -> dict[str, User]:
    ret_list: dict[str, User] = {}
    if filter is not None:
        user_query_list_object = app.db.get_list('customers', filter=filter)
    else:        
        user_query_list_object = app.db.get_list('customers')
    
    for account in user_query_list_object.items:
        user = User().read_from_query_object(account)
        ret_list.update({user.ID: user})
    return ret_list