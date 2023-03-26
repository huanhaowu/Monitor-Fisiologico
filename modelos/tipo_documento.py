from modelos.conexion import Conexion
#Arreglo - Documentar el funcionamiento

class TipoDocumento:
    
    def __init__(self, id_tipo_documento:int = 0, descripcion:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_tipo_documento = id_tipo_documento
        self.descripcion = descripcion
    
    def cargar_descripcion_tipo_documento(self):
        bd = Conexion()  #Se crea un objeto de la clase Conexion
        
        #Se ejecuta la consulta para obtener la descripción o nombre del tipo de documento
        resultado = bd.execute_query("SELECT descripcion FROM Tipo_Documento WHERE id_tipo_documento = ?", [self.id_tipo_documento]) 
        self.descripcion = resultado[0][0]

    def cargar_id_tipo_documento(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        #Se ejecuta la consulta para obtener el id del tipo de documento con la descripción determinada
        resultado = bd.execute_query("SELECT id_tipo_documento FROM Tipo_Documento WHERE descripcion = ?", [self.descripcion])
        self.id_tipo_documento = resultado[0][0]
        
    def obtener_lista_tipo_documento(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT descripcion FROM Tipo_Documento") #Se obtiene un listado de los tipos documento
        return resultado
