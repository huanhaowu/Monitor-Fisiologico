from modelos.conexion import Conexion

class OrientacionSexual:
    def __init__(self, id_orientacion_sexual:int = 0, descripcion:str = ""):
        self.id_orientacion_sexual = id_orientacion_sexual
        self.descripcion = descripcion
    
    def obtener_lista_orientaciones(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Orientacion_Sexual")
        return resultado
    
    def cargar_descripcion_orientacion_sexual(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Orientacion_Sexual WHERE id_orientacion_sexual = ?", [self.id_orientacion_sexual])
        self.descripcion = resultado[0][0]