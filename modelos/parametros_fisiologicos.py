from modelos.conexion import Conexion
#Arreglo - Documentar el funcionamiento

class ParametrosFisiologicos:
    def __init__(self, id_parametro_fisiologico:int = 0, descripcion:str = "", min_estandar:float = 0, max_estandar:float = 0, alerta_alto:float = 0, alerta_bajo:float = 0, critico_alto:float = 0, critico_bajo:float = 0, instrucciones:str = ""):
        #Se reciben los parametros y se asignan a los atributos de la clase
        #Los parametros son opcionales
        self.id_parametro_fisiologico = id_parametro_fisiologico
        self.descripcion = descripcion
        self.min_estandar = min_estandar
        self.max_estandar = max_estandar
        self.alerta_alto = alerta_alto
        self.alerta_bajo = alerta_bajo
        self.critico_alto = critico_alto
        self.critico_bajo = critico_bajo
        self.instrucciones = instrucciones
    
    def realizar_medicion_parametro(self):
        
        #TO-DO acordar la conexion con el dispositivo del monitor
        
        if self.descripcion == 'Temperatura':
            return 35
        
        elif self.descripcion == 'Presion Arterial Sistolica':
            return 80

        elif self.descripcion == 'Presion Arterial Diastolica':
            return 60
        
        elif self.descripcion == 'Frecuencia Cardiaca':
            return 60
        
        elif self.descripcion == 'Saturacion de Oxigeno':
            return 95

    def cargar_datos_parametro(self, descripcion:str):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT id_parametro_fisiologico, descripcion, min_estandar, max_estandar, alerta_alto, alerta_bajo, critico_alto, critico_bajo, instrucciones FROM Parametros_Fisiologicos WHERE descripcion = ?", [descripcion])
        if resultado: #Si la consulta devuelve un resultado
            # Se asignan los valores de la consulta a los atributos de la clase
            self.id_parametro_fisiologico = resultado[0][0]
            self.descripcion = resultado[0][1]
            self.min_estandar = resultado[0][2]
            self.max_estandar = resultado[0][3]
            self.alerta_alto = resultado[0][4]
            self.alerta_bajo = resultado[0][5]
            self.critico_alto = resultado[0][6]
            self.critico_bajo = resultado[0][7]
            self.instrucciones = resultado[0][8]
            self.instrucciones = self.instrucciones.replace('\\n',"\n") #Se reemplazan los caracteres de escape por los caracteres correspondientes
            self.instrucciones = self.instrucciones.replace('\\t',"\t") #Se reemplazan los caracteres de escape por los caracteres correspondientes
            
    
    def obtener_lista_parametros_fisiologicos(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        resultado = bd.execute_query("SELECT * Parametros_Fisiologicos") #Se ejecuta la consulta para obtener una lista de los parametros fisiologicos
        return resultado