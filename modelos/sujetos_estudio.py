from modelos.conexion import Conexion
from modelos.tipo_documento import TipoDocumento
from modelos.sexo import Sexo
from modelos.genero import Genero
from modelos.orientacion_sexual import OrientacionSexual
from modelos.nacionalidad import Nacionalidad
from modelos.provincia import Provincia
from modelos.condiciones_medicas import CondicionesMedicas
import datetime
class SujetosEstudio:
    #Arreglo - Documentar el funcionamiento

    def __init__(self, tipo_documento:str, codigo_documento:str, id_sujeto:int = 0 , nombres:str = "", apellidos:str = "", fecha_nacimiento:datetime.date = None, sexo:Sexo = None, genero:Genero = None, orientacion_sexual:OrientacionSexual = None, nacionalidad:Nacionalidad = None, provincia:Provincia = None, correo:str = "", condiciones_medicas:list[CondicionesMedicas] = []):
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
        self.condiciones_medicas = condiciones_medicas
        
    def ingresar(self):
        bd = Conexion() #Se crea un objeto de la clase Conexion
        #Se ejecuta la consulta para obtener un sujeto de estudio por su tipo de cdocumento y codigo
        resultado = bd.execute_query('''SELECT * 
                                        FROM Sujetos_Estudio
                                        WHERE id_tipo_documento = ? AND codigo_documento = ?''',  
                                        [self.tipo_documento.id_tipo_documento, self.codigo_documento]) 
        if resultado:  #Si se obtuvieron resultados
            #Se asignan los valores obtenidos a los atributos de la clase
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

            #Se hace una consulta para obtener las condiciones médicas del sujeto
            resultado = bd.execute_query('''SELECT id_condicion_medica FROM Condiciones_Sujeto WHERE id_sujeto = ?''', [self.id_sujeto]) 
            for condicion in resultado:
                p = CondicionesMedicas(condicion[0])
                p.cargar_descripcion_condicion_medica()
                self.condiciones_medicas.append(p)
            
            return True
        else:
            return False
        
    #Se registra el sujeto 
    def registrar(self, nombres:str, apellidos:str, fecha_nacimiento:datetime.date, sexo:int, genero:int, orientacion_sexual:int, nacionalidad:int, provincia:int, correo:str, condiciones:list[int]):
        bd = Conexion()
        self.nombres = nombres
        self.apellidos = apellidos
        
        self.fecha_nacimiento = fecha_nacimiento

        self.sexo = Sexo(sexo)
        self.sexo.cargar_descripcion_sexo()

        self.genero = Genero(genero)
        self.genero.cargar_descripcion_genero()

        self.orientacion_sexual = OrientacionSexual(orientacion_sexual)
        self.orientacion_sexual.cargar_descripcion_orientacion_sexual()

        self.nacionalidad = Nacionalidad(nacionalidad)
        self.nacionalidad.cargar_descripcion_nacionalidad()

        self.provincia = Provincia(provincia)
        self.provincia.cargar_descripcion_provincia()

        self.correo = correo
        self.condiciones_medicas.clear()
        
        # Se añaden sus condiciones médicas 
        for condicion in condiciones:
            p = CondicionesMedicas(condicion)
            p.cargar_descripcion_condicion_medica()
            self.condiciones_medicas.append(p)
        
        # Primero verifico si el usuario existe 
        existe = bd.execute_query('''SELECT id_sujeto FROM Sujetos_Estudio WHERE id_tipo_documento = ? AND codigo_documento = ?''', 
                                  [self.tipo_documento.id_tipo_documento, self.codigo_documento])
        
        # Si existe el usuario
        if existe:
            self.id_sujeto = existe[0][0]
            
            #Se actualizan sus datos y sus condiciones médicas
            bd.execute_command('''UPDATE Sujetos_Estudio SET nombre = ?, apellido = ?, fecha_nacimiento = ?, id_sexo = ?, id_genero = ?, id_orientacion_sexual = ?, id_nacionalidad = ?, id_provincia = ?, correo_electronico = ? WHERE id_sujeto = ?''', 
                               [self.nombres, self.apellidos, self.fecha_nacimiento, self.sexo.id_sexo, self.genero.id_genero, self.orientacion_sexual.id_orientacion_sexual, self.nacionalidad.id_nacionalidad, self.provincia.id_provincia, self.correo, self.id_sujeto])
            
            bd.execute_command('''DELETE FROM Condiciones_Sujeto WHERE id_sujeto = ?''', 
                               [self.id_sujeto])
            for condicion in self.condiciones_medicas:
                bd.execute_command(
                    '''INSERT INTO Condiciones_Sujeto (id_sujeto, id_condicion_medica) VALUES (?,?)''',
                    [self.id_sujeto, condicion.id_condicion_medica]
                )
        else:
            # Si el usuario no existe se crea un nuevo registro
            bd.execute_command('''INSERT INTO Sujetos_Estudio(nombre, apellido, fecha_nacimiento, id_tipo_documento, codigo_documento, id_sexo, id_genero, id_orientacion_sexual, id_nacionalidad, id_provincia, correo_electronico) 
                              VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                              [self.nombres, self.apellidos, self.fecha_nacimiento, self.tipo_documento.id_tipo_documento, self.codigo_documento, self.sexo.id_sexo, self.genero.id_genero, self.orientacion_sexual.id_orientacion_sexual, self.nacionalidad.id_nacionalidad, self.provincia.id_provincia, self.correo])

            # Se selecciona el usuario creado para adjuntarle sus condiciones médicas
            self.id_sujeto = int(bd.execute_query("SELECT MAX(id_sujeto) FROM Sujetos_Estudio")[0][0])
            if self.id_sujeto:
                for condicion in self.condiciones_medicas:
                    bd.execute_command(
                        '''INSERT INTO Condiciones_Sujeto (id_sujeto, id_condicion_medica) VALUES (?,?)''',
                        [self.id_sujeto, condicion.id_condicion_medica]
                    )