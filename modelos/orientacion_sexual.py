from modelos.conexion import Conexion

class OrientacionSexual:
    def __init__(self, id_orientacion_sexual:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_orientacion_sexual = id_orientacion_sexual
        self.descripcion = descripcion
    
    def obtener_lista_orientaciones(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT * FROM Orientacion_Sexual") #Se ejecuta la consulta para obtener una lista de las orientaciones sexuales
        return resultado
    
    def cargar_descripcion_orientacion_sexual(self): 
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT descripcion FROM Orientacion_Sexual WHERE id_orientacion_sexual = ?", [self.id_orientacion_sexual]) #Se ejecuta la consulta para obtener la descripcion de la orientacion sexual introducida
        self.descripcion = resultado[0][0] #Se asigna la descripcion de la orientacion sexual a la variable descripcion