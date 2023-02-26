class SujetosEstudio:
     def __init__(self, id_sujeto, nombres, apellidos, fecha_nacimiento, tipo_documento, codigo_documento, sexo, genero, orientacion_sexual, nacionalidad, provincia, correo, fecha_creacion, condiciones_medicas):
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
         return bool
     
     def registrar(self, nombres, apellidos, fecha_nacimiento, tipo_documento, codigo_documento, sexo, genero, orientacion_sexual, nacionalidad, provincia, correo, condiciones_medicas):
         return 0
     
     def agregar_condiciones(self, condicion):
         return 0