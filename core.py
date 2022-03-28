# tinyDB to be used in this example.
from tinydb import TinyDB, Query
import os, sys
from utils import Alerts


class Manager:
    
    database_name = 'records.json'
        
    def __init__(self):
        self.connection = TinyDB(self.current_directory  + os.sep + self.database_name)
        if not os.path.exists(self.current_directory + os.sep + self.database_name):
            with open(self.current_directory + os.sep + self.database_name, 'w+') as writer: pass 
        
        connection_str = str(self.connection).split(',')
        _, _, tail = connection_str[1].partition('=')
        if int(tail) == 0:
            Alerts.show_alert('warning', "Information: There's no table inside your database file . . . ")
    
    @property
    def current_directory(self):
        return os.path.dirname(os.path.realpath(sys.argv[0]))
    
    def add_record(self, text):
        self.connection.insert({'todos': text})
    
    def delete_record(self, record):
        todo = Query()
        self.connection.remove(todo.todos  == record)
    
if __name__ == '__main__':
    man = Manager()
    