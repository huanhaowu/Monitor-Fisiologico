from modelos.conexion import Conexion

class ParametrosFisiologicos:
    def __init__(self, id_parametro_fisiologico:int = 0, descripcion:str = "", min_estandar:float = 0, max_estandar:float = 0, alerta_alto:float = 0, alerta_bajo:float = 0, critico_alto:float = 0, critico_bajo:float = 0, instrucciones:str = ""):
        self.id_parametro_fisiologico = id_parametro_fisiologico
        self.descripcion = descripcion
        self.min_estandar = min_estandar
        self.max_estandar = max_estandar
        self.alerta_alto = alerta_alto
        self.alerta_bajo = alerta_bajo
        self.critico_alto = critico_alto
        self.critico_bajo = critico_bajo
        self.instrucciones = instrucciones
    
    def obtener_lista_parametros_fisiologicos(self):
        bd = Conexion()
        resultado = bd.execute_query("SELECT * Parametros_Fisiologicos")
        return resultado