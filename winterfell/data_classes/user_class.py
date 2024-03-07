from tokeo.ext.appshare import app


class User:
    def __init__(self, first_name: str = "", last_name: str = "", ID: int = 0, spent_minutes: int = 0, spent_data: int = 0, contracts: list[str] = []):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.spent_minutes = spent_minutes
        self.spent_data = spent_data
        self.contracts = contracts
    
    def update_in_db():
        ...
    
    def create_new_in_db():
        ...
        
    def remove_in_db():
        ...

def read_user_from_db(key: str) -> User:
    user_query_object = app.db.get_one('test_accounts', key)
    return User(
        first_name=user_query_object.first_name,
        last_name=user_query_object.last_name
        )
    
def read_user_list_from_db(filter = None) -> list[User]:
    ret_list: list[User] = []
    if filter is not None:
        user_query_list_object = app.db.get_list('test_accounts', filter=filter)
    else:        
        user_query_list_object = app.db.get_list('test_accounts')
    for account in user_query_list_object.items:
        ret_list.append(read_user_from_db(account.id))
    return ret_list