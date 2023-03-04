import sqlite3
import os


class Conexion:
    def __init__(self):
        self.db_file = "base_datos.db"
        
        if not os.path.isfile(self.db_file):
            self.create_database()

    def enter(self):
        self.conn = sqlite3.connect(self.db_file)


    def create_database(self):
        self.enter()
        sql_file = os.path.abspath("scripts.sql")
        with open(sql_file, 'r') as f:
            sql = f.read()
            self.conn.executescript(sql)
        self.exit()
    
    def exit(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def execute_command(self, command, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(command, params)
        else:
            cursor.execute(command)
        self.conn.commit()

