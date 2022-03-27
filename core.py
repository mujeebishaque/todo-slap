# tinyDB to be used in this example.
from tinydb import TinyDB
import os, sys
from utils import Alerts


class Manager:
    
    database_name = 'records.json'
        
    def __init__(self):
        self.connection = TinyDB(self.current_directory  + self.database_name)
        connection_str = str(self.connection).split(',')
        _, _, tail = connection_str[1].partition('=')
        if int(tail) == 0:
            return Alerts.show_alert('error', "ERROR: Can't connect to the local database. ")
        
    @property
    def current_directory(self):
        return os.path.dirname(os.path.realpath(sys.argv[0]))
    
    @staticmethod
    def add_record(text):
        pass
    
    @staticmethod
    def delete_record(record_id):
        pass
    
if __name__ == '__main__':
    man = Manager()
    