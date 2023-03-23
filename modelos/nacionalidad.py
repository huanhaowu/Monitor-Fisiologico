from modelos.conexion import Conexion
class Nacionalidad:
    def __init__(self, id_nacionalidad:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_nacionalidad = id_nacionalidad
        self.descripcion = descripcion

    def obtener_lista_nacionalidades(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT * FROM Nacionalidad") #Se ejecuta la consulta para obtener una lista de las nacionalidades
        return resultado
    
    def cargar_descripcion_nacionalidad(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT descripcion FROM Nacionalidad WHERE id_nacionalidad = ?", [self.id_nacionalidad]) #Se ejecuta la consulta para obtener la descripcion de la nacionalidad introducida
        self.descripcion = resultado[0][0] #Se asigna la descripcion de la nacionalidad a la variable descripcion

