from modelos.conexion import Conexion

#Arreglo - Documentar el funcionamiento

class Provincia:
    def __init__(self, id_provincia:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_provincia = id_provincia
        self.descripcion = descripcion
    
    def obtener_lista_provincias(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT * FROM Provincia") #Se ejecuta la consulta para obtener una lista de las provincias
        return resultado
    
    def cargar_descripcion_provincia(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT descripcion FROM Provincia WHERE id_provincia = ?", [self.id_provincia]) #Se ejecuta la consulta para obtener la descripción o nombre de la provincia
        self.descripcion = resultado[0][0]