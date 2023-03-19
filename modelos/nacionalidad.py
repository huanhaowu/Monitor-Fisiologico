from modelos.conexion import Conexion
class Nacionalidad:
    #Arreglo - Documentar el funcionamiento

    def __init__(self, id_nacionalidad:int = 0, descripcion:str = ""):
        self.id_nacionalidad = id_nacionalidad
        self.descripcion = descripcion

    def obtener_lista_nacionalidades(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Nacionalidad")
        return resultado
    
    def cargar_descripcion_nacionalidad(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Nacionalidad WHERE id_nacionalidad = ?", [self.id_nacionalidad])
        self.descripcion = resultado[0][0]

