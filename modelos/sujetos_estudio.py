from conexion import Conexion
from tipo_documento import TipoDocumento
from sexo import Sexo
from genero import Genero
from orientacion_sexual import OrientacionSexual
from nacionalidad import Nacionalidad
from provincia import Provincia
from condiciones_medicas import CondicionesMedicas
class SujetosEstudio:
     def __init__(self, tipo_documento, codigo_documento, id_sujeto = 0, nombres = "", apellidos = "", fecha_nacimiento = None, sexo = None, genero = None, orientacion_sexual = None, nacionalidad = None, provincia = None, correo = "", fecha_creacion = None, condiciones_medicas = []):
        self.id_sujeto = id_sujeto
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_documento = tipo_documento
        self.codigo_documento = codigo_documento
        self.sexo = sexo
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.nacionalidad = nacionalidad
        self.provincia = provincia
        self.correo = correo
        self.fecha_creacion = fecha_creacion
        self.condiciones_medicas = condiciones_medicas
        
        
        
     def ingresar(self, codigo_documento, tipo_documento):
        bd = Conexion()
        resultado = bd.execute_query('''SELECT id_tipo_documento, codigo_documento
                            FROM Sujetos_Estudio
                            WHERE id_tipo_documento = ? AND codigo_documento = ?''', [self.tipo_documento, self.codigo_documento])
        if resultado:
            self.tipo_documento = TipoDocumento(resultado[0][0])
            self.codigo_documento = resultado[0][1]
            return True
        else:
            return False
     
     def registrar(self, nombres, apellidos, fecha_nacimiento, tipo_documento, codigo_documento, sexo, genero, orientacion_sexual, nacionalidad, provincia, correo, condiciones_medicas):
        bd = Conexion()
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_documento = tipo_documento
        self.codigo_documento = codigo_documento
        self.sexo = sexo
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.nacionalidad = nacionalidad
        self.provincia = provincia
        self.correo = correo
        self.condiciones_medicas = condiciones_medicas 
        resultado = bd.execute_command('''INSERT INTO Sujetos_Estudio(nombre, apellido, fecha_nacimiento, id_tipo_documento, codigo_documento, id_sexo, id_genero, id_orientacion_sexual, id_nacionalidad, id_provincia, correo_electronico) 
                                          VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                                          [self.nombres, self.apellidos, self.fecha_nacimiento, self.tipo_documento.id_tipo_documento, self.codigo_documento, self.sexo.id_sexo, self.genero.id_genero, self.orientacion_sexual.id_orientacion_sexual, self.nacionalidad.id_nacionalidad, self.provincia.id_provincia, self.correo])
        
        self.id_sujeto = int(bd.execute_query("SELECT MAX(id_sujeto) FROM Sujetos_Estudio")[0][0])
        if self.id_sujeto:
            for parametro in condiciones_medicas:
                bd.execute_command(
                    '''INSERT INTO Condiciones_Sujeto (id_sujeto, id_condicion_medica) VALUES (?,?)''',
                    [self.id_sujeto, parametro.parametro.id_condicion_medicas]
                )
     
     #def agregar_condiciones(self, condicion):
        #return 0