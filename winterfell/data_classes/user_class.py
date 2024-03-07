from tokeo.ext.appshare import app
from database_object import DatabaseObject


class User(DatabaseObject):
    def __init__(self):
        self.ID: str = "" 
        self.forename: str = ""
        self.surname: str = ""
        self.address: str = ""
        self.zipcode: str = ""
        self.city: str = ""
        self.email: str = ""
    
    def read_from_query_object(self, query_object):
        self.ID = query_object.id
        self.forename = query_object.forename
        self.surname = query_object.surname
        self.address = query_object.address
        self.zipcode = query_object.zipcode
        self.city = query_object.city
        self.email = query_object.email
        return self
        
    def read_in_db(self, key:str):
        self.read_from_query_object(app.db.get_one('customers', key))
    
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
        
    def delete_in_db(self):
        app.db.delete('customers', self.ID)


def read_user_list_from_db(filter = None) -> list[User]:
    ret_list: list[User] = []
    if filter is not None:
        user_query_list_object = app.db.get_list('test_accounts', filter=filter)
    else:        
        user_query_list_object = app.db.get_list('test_accounts')
    
    for account in user_query_list_object.items:
        ret_list.append(User().read_from_query_object(account))
    return ret_list