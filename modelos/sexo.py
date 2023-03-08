from modelos.conexion import Conexion

class Sexo:
    def __init__(self, id_sexo = 0, descripción = ""):
        self.id_sexo = id_sexo
        self.descripción = descripción

    def cargar_descripcion_sexo(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Sexo WHERE id_sexo = ?", [self.id_sexo])
        self.descripcion = resultado[0][0]

    def obtener_lista_sexos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Sexo")
        return resultado
