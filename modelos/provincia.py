from conexion import Conexion

class Provincia:
    def __init__(self, id_provincia = 0, descripcion = ""):
        self.id_provincia = id_provincia
        self.descripcion = descripcion
    
    def obtener_lista_provincias(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Provincia")
        return resultado