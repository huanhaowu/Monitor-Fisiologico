from modelos.conexion import Conexion

class Sexo:
    def __init__(self, id_sexo:int = 0, descripcion:str = ""):
        self.id_sexo = id_sexo
        self.descripcion = descripcion

    def cargar_descripcion_sexo(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Sexo WHERE id_sexo = ?", [self.id_sexo])
        self.descripcion = resultado[0][0]

    def obtener_lista_sexos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Sexo")
        return resultado
