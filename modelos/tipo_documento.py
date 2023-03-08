from modelos.conexion import Conexion

class TipoDocumento:
    
    def __init__(self, id_tipo_documento:int = 0, descripcion:str = ""):
        self.id_tipo_documento = id_tipo_documento
        self.descripcion = descripcion
    
    def cargar_descripcion_tipo_documento(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Tipo_Documento WHERE id_tipo_documento = ?", [self.id_tipo_documento])
        self.descripcion = resultado[0][0]

    def cargar_id_tipo_documento(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT id_tipo_documento FROM Tipo_Documento WHERE descripcion = ?", [self.descripcion])
        self.id_tipo_documento = resultado[0][0]
        
    def obtener_lista_tipo_documento(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT descripcion FROM Tipo_Documento")
        return resultado
