from modelos.conexion import Conexion
#Arreglo - Documentar el funcionamiento

class TipoUsuario:
    def __init__(self, id_tipo_usuario:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_tipo_usuario = id_tipo_usuario
        self.descripcion = descripcion
    
    
    def obtener_lista_tipo_usuarios(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT * FROM Tipo_Usuario") #Se obtiene un listado de los tipos de usuarios
        return resultado