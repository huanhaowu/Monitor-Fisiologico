from modelos.conexion import Conexion
class Genero:
    def __init__(self, id_genero:int = 0, descripcion:str = ""):
        self.id_genero = id_genero
        self.descripcion = descripcion
    
    def obtener_lista_generos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM genero")
        return resultado
    
    def cargar_descripcion_genero(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Genero WHERE id_genero = ?", [self.id_genero])
        self.descripcion = resultado[0][0]

#prueba = Genero()
#print(prueba.obtener_lista_generos())