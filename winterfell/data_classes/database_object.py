from abc import ABC, abstractmethod

class DatabaseObject(ABC):
    @abstractmethod
    def update_in_db(self):
        ...
    
    @abstractmethod
    def delete_in_db(self):
        ...
        
    