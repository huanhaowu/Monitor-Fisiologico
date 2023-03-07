from modelos.conexion import Conexion

class TipoDocumento:
    
    def __init__(self,id_TipoDocumento = 0,descripción = ""):
        self.id_tipo_documento = id_TipoDocumento
        self.descripcion = descripción
    
    def obtener_lista_tipo_documento(self):
        bd = Conexion()
        
        resultado = bd.execute_query("SELECT descripcion FROM Tipo_Documento")
        return resultado
