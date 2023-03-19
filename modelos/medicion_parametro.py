from modelos.parametros_fisiologicos import ParametrosFisiologicos
#Arreglo - Documentar el funcionamiento

class MedicionParametro:
    def __init__(self, parametro:ParametrosFisiologicos, medida_parametro_fisiologico:float):
        self.parametro = parametro
        self.medida_parametro_fisiologico = medida_parametro_fisiologico

    def asignar_color(self):
        # '' normal, + alto, - bajo
        # amarillo -> #FFBF00 ; verde -> #00C040 ; rojo -> #FF0211 ; gris -> #F5F5F5
        if self.medida_parametro_fisiologico <= self.parametro.critico_bajo:
            return ("gris", '', self.medida_parametro_fisiologico)

        if self.parametro.critico_bajo < self.medida_parametro_fisiologico < self.parametro.alerta_bajo:
            return ("rojo", '-', self.medida_parametro_fisiologico)

        if self.parametro.alerta_bajo <= self.medida_parametro_fisiologico < self.parametro.min_estandar:
            return ("amarillo", '-', self.medida_parametro_fisiologico)

        if self.parametro.min_estandar <= self.medida_parametro_fisiologico <= self.parametro.max_estandar:
            return ("verde", '', self.medida_parametro_fisiologico)

        if (self.parametro.alerta_alto):
            if self.parametro.max_estandar < self.medida_parametro_fisiologico <= self.parametro.alerta_alto:
                return ("amarillo", '+', self.medida_parametro_fisiologico)

            if (self.parametro.critico_alto):
                if self.parametro.alerta_alto < self.medida_parametro_fisiologico <= self.parametro.critico_alto:
                    return ("rojo", '+', self.medida_parametro_fisiologico)

                if self.parametro.critico_alto < self.medida_parametro_fisiologico:
                    return ("rojo", '', self.medida_parametro_fisiologico)
            else:
                if self.parametro.alerta_alto < self.medida_parametro_fisiologico:
                    return ("rojo", '+', self.medida_parametro_fisiologico)
        else:
            if self.parametro.max_estandar < self.medida_parametro_fisiologico:
                return ("gris", '', self.medida_parametro_fisiologico)
