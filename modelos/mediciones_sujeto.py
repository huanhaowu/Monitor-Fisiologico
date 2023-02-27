class MedicionesSujeto:
    def __init__(self, id_medicion = 0, sujeto = None, peso_sujeto = 0, altura_sujeto = 0, fecha_medicion = None, parametros_medidos = []):
        self.id_medicion = id_medicion
        self.sujeto = sujeto
        self.peso_sujeto = peso_sujeto
        self.altura_sujeto = altura_sujeto
        self.fecha_medicion = fecha_medicion
        self.parametros_medidos = parametros_medidos

    def guardar_medicion(self,sujeto, peso_sujeto, altura_sujeto, fecha_medicion, parametros_medidos):
        pass

    def retornar_medicion(self, id_medicion):
        pass
