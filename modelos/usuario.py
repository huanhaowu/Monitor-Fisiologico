class Usuario:
    def __init__(self, usuario, clave, id_usuario = 0, nombre = "", apellido = "", fecha_nacimiento = None, id_creador = 0, correo_electronico = "", telefono = "", activo = True, fecha_creacion = None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.id_creador = id_creador
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.activo = activo
        self.fecha_creacion = fecha_creacion
        self.clave = clave
    
    def ingresar(self, usuario, clave):
        pass