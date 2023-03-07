from modelos.conexion import Conexion

class OrientacionSexual:
    def __init__(self, id_orientacion_sexual = 0, descripcion = ""):
        self.id_orientacion_sexual = id_orientacion_sexual
        self.descripcion = descripcion
    
    def obtener_lista_orientaciones(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Orientacion_Sexual")
        return resultado