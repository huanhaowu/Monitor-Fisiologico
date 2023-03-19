from modelos.conexion import Conexion
#Arreglo - Documentar el funcionamiento

class TipoUsuario:
    def __init__(self, id_tipo_usuario:int = 0, descripcion:str = ""):
        self.id_tipo_usuario = id_tipo_usuario
        self.descripcion = descripcion
    
    
    def obtener_lista_tipo_usuarios(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Tipo_Usuario")
        return resultado