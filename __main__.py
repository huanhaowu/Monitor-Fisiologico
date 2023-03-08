from interfaces.login_suj import LoginSujEstudio
def main():
    login = LoginSujEstudio()
    
if __name__ == "__main__":
    # region IMPORTS CLASES
    from datetime import date, datetime
    from modelos.sujetos_estudio import SujetosEstudio
    from modelos.mediciones_sujeto import MedicionesSujeto
    from modelos.medicion_parametro import MedicionParametro
    from modelos.parametros_fisiologicos import ParametrosFisiologicos
    from modelos.tipo_documento import TipoDocumento
    from modelos.sexo import Sexo
    from modelos.genero import Genero
    from modelos.orientacion_sexual import OrientacionSexual
    from modelos.nacionalidad import Nacionalidad
    from modelos.provincia import Provincia
    from modelos.condiciones_medicas import CondicionesMedicas
    from interfaces.reporte_med import ReporteMed

    # endregion
    sexo = Sexo(0, "Hombre")
    genero = Genero(0, "Masculino")
    orientacion = OrientacionSexual(0, "Heterosexual")
    provincia = Provincia(0, "Santo Domingo")
    nacionalidad = Nacionalidad(0, "Dominicano")
    parametro1 = ParametrosFisiologicos(1, "Temperatura", 36, 37, 40, 34, 46, 29.99, "Instruccion")
    parametro2 = ParametrosFisiologicos(2, "Presion Arterial", 36, 37, 40, 34, 46, 29.99, "Instruccion")
    lista_parametros = [parametro1, parametro2]
    condicion1 = CondicionesMedicas(0, "Asma", lista_parametros)
    condicion2 = CondicionesMedicas(1, "Diabetes", lista_parametros)
    lista_condiciones = [condicion1, condicion2]
    tipo_documento = TipoDocumento(0, "Cedula")
    fecha_nacimiento = datetime.strptime("1990/01/01", '%Y/%m/%d')

    sujeto1 = SujetosEstudio(tipo_documento.descripcion, "1234532", 1, "Juan", "Perez", fecha_nacimiento,
                             sexo, genero, orientacion, nacionalidad, provincia, "paolasaldanaquezada@gmail.com",
                             lista_condiciones)

    medicion_parametros1 = MedicionParametro(1, parametro1, 36)
    medicion_parametros2 = MedicionParametro(2, parametro2, 45)
    listaMediciones = [medicion_parametros1, medicion_parametros2]
    medicion1 = MedicionesSujeto(1, sujeto1, 70, 180, date.today(), listaMediciones)
    reporte = ReporteMed(sujeto1, medicion1)
    reporte.crear_pdf()




