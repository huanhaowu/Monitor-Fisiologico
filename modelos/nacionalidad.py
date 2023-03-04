from conexion import Conexion
class Nacionalidad:
    
    def __init__(self, id_nacionalidad = 0, descripcion = ""):
        self.id_nacionalidad = id_nacionalidad
        self.descripcion = descripcion

    def obtener_lista_nacionalidades(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Nacionalidad")
        return resultado