from modelos.conexion import Conexion
from modelos.medicion_parametro import MedicionParametro
from modelos.parametros_fisiologicos import ParametrosFisiologicos
from modelos.sujetos_estudio import SujetosEstudio
import datetime
class MedicionesSujeto:
    def __init__(self, id_medicion:int = 0, sujeto:SujetosEstudio = None, peso_sujeto:float = 0, altura_sujeto:float = 0, fecha_medicion:datetime.date = None, parametros_medidos:list[MedicionParametro] = []):
        self.id_medicion = id_medicion
        self.sujeto = sujeto
        self.peso_sujeto = peso_sujeto
        self.altura_sujeto = altura_sujeto
        self.fecha_medicion = fecha_medicion
        self.parametros_medidos = parametros_medidos

    def guardar_medicion(self, sujeto:SujetosEstudio, peso_sujeto:float, altura_sujeto:float, fecha_medicion:datetime.date, parametros_medidos:list[MedicionParametro]):
        bd = Conexion()
        self.sujeto = sujeto
        self.peso_sujeto = peso_sujeto
        self.altura_sujeto = altura_sujeto
        self.fecha_medicion = fecha_medicion
        self.parametros_medidos = parametros_medidos
        bd.execute_command(
            "INSERT INTO Mediciones_Sujeto (id_sujeto, peso_sujeto, altura_sujeto, fecha_medicion) VALUES (?,?,?,?)", 
            [self.sujeto.id_sujeto, self.peso_sujeto, self.altura_sujeto, self.fecha_medicion])

        self.id_medicion = int(bd.execute_query("SELECT MAX(id_medicion) FROM Mediciones_Sujeto")[0][0]) 
        if self.id_medicion:
            for parametro in parametros_medidos:
                bd.execute_command(
                    "INSERT INTO Medicion_Parametro (id_medicion, id_parametro_fisiologico, medida_parametro_fisiologico) VALUES (?,?,?)",
                [self.id_medicion, parametro.id_parametro_fisiologico, parametro.medida_parametro_fisiologico])

    def cargar_datos_medicion(self, id_medicion):
        bd = Conexion()
        resultado = bd.execute_query("SELECT id_medicion, id_sujeto, peso_sujeto, altura_sujeto, fecha_medicion " +
                                     "FROM Mediciones_Sujeto WHERE id_medicion = ?", [id_medicion])
        if resultado:
            self.id_medicion = resultado[0][0]
            self.sujeto = SujetosEstudio(resultado[0][1])
            self.peso_sujeto = resultado[0][2]
            self.altura_sujeto = resultado[0][3]
            self.fecha_medicion = resultado[0][4]
            self.cargar_detalle_medicion(self.id_medicion)

    def cargar_ultima_medicion_sujeto(self, sujeto:SujetosEstudio):
        bd = Conexion()
        resultado = bd.execute_query("SELECT id_medicion, peso_sujeto, altura_sujeto, fecha_medicion " +
                                     "FROM Mediciones_Sujeto WHERE id_sujeto = ? ORDER BY fecha_medicion DESC LIMIT 1", [sujeto.id_sujeto])
        if resultado:
            self.id_sujeto = sujeto.id_sujeto
            self.id_medicion = resultado[0][0]
            self.peso_sujeto = resultado[0][1]
            self.altura_sujeto = resultado[0][2]
            self.fecha_medicion = resultado[0][3]
            self.cargar_detalle_medicion(self.id_medicion)

    def cargar_detalle_medicion(self, id_medicion:int):
        bd = Conexion()
        resultado = bd.execute_query("SELECT MP.id_detalle_medicion, P.id_parametro_fisiologico, P.descripcion, P.min_estandar, P.max_estandar, P.alerta_bajo, P.alerta_alto, P.critico_bajo, P.critico_alto, P.instrucciones, MP.medida_parametro_fisiologico " +
                                    "FROM Medicion_Parametro as MP " +
                                    "INNER JOIN Parametros_Fisiologicos as P ON MP.id_parametro_fisiologico = P.id_parametro_fisiologico " + 
                                    "WHERE id_medicion = ?", [self.id_medicion])
        for parametro in resultado:
            p = ParametrosFisiologicos(parametro[1], parametro[2], parametro[3], parametro[4], parametro[5], parametro[6], parametro[7], parametro[8], parametro[9])
            mp = MedicionParametro(parametro[0], p, parametro[10])
            self.parametros_medidos.append(mp)