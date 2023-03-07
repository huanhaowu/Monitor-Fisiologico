from modelos.conexion import Conexion
from modelos.tipo_documento import TipoDocumento
from modelos.sexo import Sexo
from modelos.genero import Genero
from modelos.orientacion_sexual import OrientacionSexual
from modelos.nacionalidad import Nacionalidad
from modelos.provincia import Provincia
from modelos.condiciones_medicas import CondicionesMedicas
class SujetosEstudio:
    
    def __init__(self, tipo_documento, codigo_documento, id_sujeto = 0, nombres = "", apellidos = "", fecha_nacimiento = None, sexo = None, genero = None, orientacion_sexual = None, nacionalidad = None, provincia = None, correo = "", fecha_creacion = None, condiciones_medicas = []):
        #Parametros obligatorios
        self.tipo_documento = TipoDocumento(descripcion = tipo_documento)
        self.tipo_documento.cargar_id_tipo_documento()
        self.codigo_documento = codigo_documento
        
        #Parametros opcionales
        self.id_sujeto = id_sujeto
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.nacionalidad = nacionalidad
        self.provincia = provincia
        self.correo = correo
        self.fecha_creacion = fecha_creacion
        self.condiciones_medicas = condiciones_medicas
        
    def ingresar(self):
        bd = Conexion()
        resultado = bd.execute_query('''SELECT id_sujeto, nombre, apellido, fecha_nacimiento, id_tipo_documento, 
                                            codigo_documento, id_sexo, id_genero, id_orientacion_sexual, id_nacionalidad, id_provincia, correo_electronico 
                                        FROM Sujetos_Estudio
                                        WHERE id_tipo_documento = ? AND codigo_documento = ?''', 
                                        [self.tipo_documento.id_tipo_documento, self.codigo_documento])
        if resultado:
            self.id_sujeto = resultado[0][0]
            self.nombres = resultado[0][1]
            self.apellidos = resultado[0][2]
            self.fecha_nacimiento = resultado[0][3]
            
            self.tipo_documento = TipoDocumento(resultado[0][4])
            self.tipo_documento.cargar_descripcion_tipo_documento()
            
            self.codigo_documento = resultado[0][5]
            
            self.sexo = Sexo(resultado[0][6])
            self.sexo.cargar_descripcion_sexo()
           
            self.genero = Genero(resultado[0][7])
            self.genero.cargar_descripcion_genero()
            
            self.orientacion_sexual = OrientacionSexual(resultado[0][8])
            self.orientacion_sexual.cargar_descripcion_orientacion_sexual()
            
            self.nacionalidad = Nacionalidad(resultado[0][9])
            self.nacionalidad.cargar_descripcion_nacionalidad()
            
            self.provincia = Provincia(resultado[0][10])
            self.provincia.cargar_descripcion_provincia()
            
            self.correo = resultado[0][11]
            self.fecha_creacion = resultado[0][12]
            return True
        else:
            return False
     
    def registrar(self, nombres, apellidos, fecha_nacimiento, sexo, genero, orientacion_sexual, nacionalidad, provincia, correo, condiciones_medicas):
        bd = Conexion()
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.nacionalidad = nacionalidad
        self.provincia = provincia
        self.correo = correo
        self.condiciones_medicas = condiciones_medicas
        
        #Primero verifico si el usuario existe
        existe = bd.execute_query('''SELECT id_sujeto FROM Sujetos_Estudio WHERE id_tipo_documento = ? AND codigo_documento = ?''', 
                                  [self.tipo_documento.id_tipo_documento, self.codigo_documento])
        
        if existe:
            self.id_sujeto = existe[0][0]
            bd.execute_command('''UPDATE Sujetos_Estudio SET nombre = ?, apellido = ?, fecha_nacimiento = ?, id_sexo = ?, id_genero = ?, id_orientacion_sexual = ?, id_nacionalidad = ?, id_provincia = ?, correo_electronico = ? WHERE id_sujeto = ?''', 
                               [self.nombres, self.apellidos, self.fecha_nacimiento, self.sexo.id_sexo, self.genero.id_genero, self.orientacion_sexual.id_orientacion_sexual, self.nacionalidad.id_nacionalidad, self.provincia.id_provincia, self.correo, self.id_sujeto])
            for condicion in condiciones_medicas:
                bd.execute_command(
                    '''INSERT INTO Condiciones_Sujeto (id_sujeto, id_condicion_medica) VALUES (?,?)''',
                    [self.id_sujeto, condicion.id_condicion_medica]
                )
        else:
            bd.execute_command('''INSERT INTO Sujetos_Estudio(nombre, apellido, fecha_nacimiento, id_tipo_documento, codigo_documento, id_sexo, id_genero, id_orientacion_sexual, id_nacionalidad, id_provincia, correo_electronico) 
                              VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                              [self.nombres, self.apellidos, self.fecha_nacimiento, self.tipo_documento.id_tipo_documento, self.codigo_documento, self.sexo.id_sexo, self.genero.id_genero, self.orientacion_sexual.id_orientacion_sexual, self.nacionalidad.id_nacionalidad, self.provincia.id_provincia, self.correo])
        
            self.id_sujeto = int(bd.execute_query("SELECT MAX(id_sujeto) FROM Sujetos_Estudio")[0][0])
            if self.id_sujeto:
                for condicion in condiciones_medicas:
                    bd.execute_command(
                        '''INSERT INTO Condiciones_Sujeto (id_sujeto, id_condicion_medica) VALUES (?,?)''',
                        [self.id_sujeto, condicion.id_condicion_medicas]
                    )