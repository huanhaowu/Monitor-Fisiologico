from parametros_fisiologicos import ParametrosFisiologicos
class MedicionParametro:
    def __init__(self, id_detalle_medicion = 0, parametro = None, medida_parametro_fisiologico = 0):
        self.id_detalle_medicion = id_detalle_medicion
        self.parametro = parametro
        self.medida_parametro_fisiologico = medida_parametro_fisiologico

    def asignar_color(self):
        # 0 normal, 1 alto, -1 bajo
        if self.medida_parametro_fisiologico <= self.parametro.critico_bajo:
            return ("gris", 0)
        
        if self.parametro.critico_bajo < self.medida_parametro_fisiologico <  self.parametro.alerta_bajo:
            return ("rojo", -1)
        
        if self.parametro.alerta_bajo <= self.medida_parametro_fisiologico <  self.parametro.min_estandar:
            return ("amarillo", -1)

        if self.parametro.min_estandar <= self.medida_parametro_fisiologico <= self.parametro.max_estandar:
            return ("green", 0)
        
        if(self.parametro.alerta_alto):
            if self.parametro.max_estandar < self.medida_parametro_fisiologico <= self.parametro.alerta_alto:
                return ("amarillo", 1)
            
            if(self.parametro.critico_alto):
                if self.parametro.alerta_alto < self.medida_parametro_fisiologico <= self.parametro.critico_alto:
                    return ("rojo", 1)
                
                if self.parametro.critico_alto < self.medida_parametro_fisiologico:
                    return ("gris", 1)
            else:
                if self.parametro.alerta_alto < self.medida_parametro_fisiologico:
                    return ("rojo", 1)
        else:
            if self.parametro.max_estandar < self.medida_parametro_fisiologico:
                return ("gris", 0)

prueba = MedicionParametro(1, ParametrosFisiologicos(1, "Temperatura", 36, 37, 40, 34, 46, 29.99), 50)

print(prueba.asignar_color())