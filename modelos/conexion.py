import sqlite3
import os

class Conexion:
    def __init__(self):
        self.db_file = "base_datos.db" #Nombre del archivo de la base de datos
        
        if not os.path.isfile(self.db_file): #Si no existe el archivo de la base de datos
            self.create_database() #Se crea la base de datos por medio del script

    def enter(self):
        self.conn = sqlite3.connect(self.db_file, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) #Se crea la conexion con la base de datos
        self.conn.text_factory = lambda x: x.decode("utf-8") #Establecer la codificación para la conexión
        

    def create_database(self):
        self.enter() #Se crea la conexion con la base de datos
        sql_file = os.path.abspath("scripts.sql") #Se obtiene la ruta del archivo con el script
        with open(sql_file, 'r', encoding="utf-8") as f: #Se abre el archivo
            sql = f.read() #Se lee el archivo
            self.conn.executescript(sql) #Se ejecuta el script
            self.conn.execute("PRAGMA encoding='UTF-8';") # Se establece la codificación de la base de datos a UTF-8
        self.exit() #Se cierra la conexion con la base de datos
    
    def exit(self):
        if self.conn: #Si existe una conexion con la base de datos
            self.conn.close() #Se cierra la conexion con la base de datos

    def execute_query(self, query:str, params:list = None):
        self.enter() #Se crea la conexion con la base de datos
        cursor = self.conn.cursor() #Se crea un cursor para ejecutar las consultas
        if params: #Si se reciben parametros
            cursor.execute(query, params) #Se ejecuta la consulta con los parametros
        else: #Si no se reciben parametros
            cursor.execute(query) #Se ejecuta la consulta
        rows = cursor.fetchall() #Se obtienen los resultados de la consulta
        self.exit() #Se cierra la conexion con la base de datos
        return rows #Se regresan los resultados de la consulta

    def execute_command(self, command:str, params:list = None):
        self.enter() #Se crea la conexion con la base de datos
        cursor = self.conn.cursor() #Se crea un cursor para ejecutar las consultas
        if params: #Si se reciben parametros
            cursor.execute(command, params) #Se ejecuta la consulta con los parametros
        else: #Si no se reciben parametros
            cursor.execute(command) #Se ejecuta la consulta
        self.conn.commit() #Se confirman los cambios en la base de datos
        self.exit() #Se cierra la conexion con la base de datos

