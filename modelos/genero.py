from modelos.conexion import Conexion
class Genero:
    def __init__(self, id_genero = 0, descripcion = ""):
        self.id_genero = id_genero
        self.descripcion = descripcion
    
    def obtener_lista_generos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM genero")
        return resultado

#prueba = Genero()
#print(prueba.obtener_lista_generos())