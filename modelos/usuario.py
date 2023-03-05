from conexion import Conexion
from tipo_usuario import TipoUsuario

class Usuario:
    def __init__(self, usuario, clave, id_usuario = 0, tipo_usuario = None, nombre = "", apellido = "", fecha_nacimiento = None, id_creador = 0, correo_electronico = "", telefono = "", activo = True, fecha_creacion = None):
        self.id_usuario = id_usuario
        self.tipo_usuario = tipo_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.clave = clave
        self.id_creador = id_creador
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.activo = activo
        self.fecha_creacion = fecha_creacion
        
    
    def ingresar(self, usuario, clave):
       bd = Conexion()
       resultado = bd.execute_query("SELECT * FROM Usuarios WHERE usuario = ? AND contrasena = ?", [self.usuario, self.clave])
       
       if resultado:
            self.id_usuario = resultado[0][0]
            self.nombre = resultado[0][1]
            self.apellido = resultado[0][2]
            self.fecha_nacimiento = resultado[0][3]
            self.clave = resultado[0][5]
            self.id_creador = resultado[0][6]
            self.correo_electronico = resultado[0][7]
            self.telefono = resultado[0][8]
            self.activo = resultado[0][9]
            self.fecha_creacion = resultado[0][10]
            
            return True
       else:
            return False