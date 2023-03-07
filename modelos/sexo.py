from modelos.conexion import Conexion

class Sexo:
    def __init__(self, id_sexo = 0, descripción = ""):
        self.id_sexo = id_sexo
        self.descripción = descripción

    def obtener_lista_sexos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Sexo")
        return resultado
