from modelos.conexion import Conexion
class Genero:
    def __init__(self, id_genero:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_genero = id_genero
        self.descripcion = descripcion
    
    def obtener_lista_generos(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT * FROM genero") #Se ejecuta la consulta para obtener una lista de los generos
        return resultado
    
    def cargar_descripcion_genero(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT descripcion FROM Genero WHERE id_genero = ?", [self.id_genero]) #Se ejecuta la consulta para obtener la descripcion del genero introducido
        self.descripcion = resultado[0][0] #Se asigna la descripcion del genero a la variable descripcion