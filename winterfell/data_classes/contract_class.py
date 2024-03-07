from database_object import DatabaseObject
from tokeo.ext.appshare import app

class Contract(DatabaseObject):
    def __init__(self) -> None:
        self.ID = ""
        self.customer = ""
        self.subscription = ""
        self.basic_fee = ""
        self.minutes_included = ""
        self.price_per_extra_minute = ""
        self.data_volume = ""
        self.imsi = ""
        self.terminal_type = ""
        self.additional_data_booked = ""
    
    def read_from_query_object(self, query_object):
        self.ID = query_object.id
        self.customer = query_object.customer
        self.subscription = query_object.subscription
        self.basic_fee = query_object.basic_fee
        self.minutes_included = query_object.minutes_included
        self.price_per_extra_minute = query_object.price_per_extra_minute
        self.data_volume = query_object.data_volume
        self.imsi = query_object.imsi
        self.terminal_type = query_object.terminal_type
        self.additional_data_booked = query_object.additional_data_booked
        return self
    
    def read_in_db(self, key):
        self.read_from_query_object(app.db.get_one('contracts', key))
        return self
    
    def create_in_db(self):
        col_dict = {
            'customer': self.customer,
            'subscription': self.subscription,
            'basic_fee': self.basic_fee,
            'minutes_included': self.minutes_included,
            'price_per_extra_minute': self.price_per_extra_minute,
            'data_volume': self.data_volume,
            'imsi': self.imsi,
            'terminal_type': self.terminal_type,
            'additional_data_booked': self.additional_data_booked
            }
        app.db.create('contracts', col_dict)
        return self
    
    def update_in_db(self, col_list: list[str]=None):
        col_dict = {
            'customer': self.customer,
            'subscription': self.subscription,
            'basic_fee': self.basic_fee,
            'minutes_included': self.minutes_included,
            'price_per_extra_minute': self.price_per_extra_minute,
            'data_volume': self.data_volume,
            'imsi': self.imsi,
            'terminal_type': self.terminal_type,
            'additional_data_booked': self.additional_data_booked
            }
        if col_list is not None:
            col_dict_new = dict(col_dict)
            for col in col_list:
                col_dict_new.update({col: col_dict.get(col)})
            col_dict = col_dict_new
        app.db.update('contracts', self.ID, col_dict)
        return self
    
    def delete_in_db(self):
        app.db.delete('contracts', self.ID)
        return self

def get_all_contracts_in_db(filter=None) -> dict[str, Contract]:
    ret_dict: dict[str, Contract] = {}
    if filter is not None:
        user_query_list_object = app.db.get_list('contracts', filter=filter)
    else:        
        user_query_list_object = app.db.get_list('contracts')
    
    for contract in user_query_list_object.items:
        contract = Contract().read_from_query_object(contract)
        ret_dict.update({contract.ID: contract})
    return ret_dict
        