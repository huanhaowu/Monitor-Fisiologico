from conexion import Conexion

class TipoUsuario:
    def __init__(self, id_tipo_usuario = 0, descripcion = ""):
        self.id_tipo_usuario = id_tipo_usuario
        self.descripcion = descripcion
    
    def obtener_lista_tipo_usuarios(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Tipo_Usuario")
        return resultado