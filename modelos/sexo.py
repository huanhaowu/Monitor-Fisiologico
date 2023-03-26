from modelos.conexion import Conexion
#Arreglo - Documentar el funcionamiento

class Sexo:
    def __init__(self, id_sexo:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_sexo = id_sexo
        self.descripcion = descripcion

    def cargar_descripcion_sexo(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT descripcion FROM Sexo WHERE id_sexo = ?", [self.id_sexo])#Se ejecuta la consulta para obtener la descripción o nombre del sexo
        self.descripcion = resultado[0][0]

    def obtener_lista_sexos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * FROM Sexo") #Se ejecuta la consulta para obtener el listado de los sexos
        return resultado
