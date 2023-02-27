class ParametrosFisiologicos:
    def __init__(self, id_parametro_fisiologico = 0, descripcion = "", min_estandar = 0, max_estandar = 0, alerta_alto = 0, alerta_bajo = 0, critico_alto = 0, critico_bajo = 0, instrucciones = ""):
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
        pass