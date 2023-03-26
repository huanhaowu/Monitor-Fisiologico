from modelos.conexion import Conexion
from modelos.tipo_usuario import TipoUsuario
#Arreglo - Documentar el funcionamiento
class Usuario:
    def __init__(self, usuario, clave, id_usuario = 0, tipo_usuario = None, nombre = "", apellido = "", fecha_nacimiento = None, id_creador = 0, correo_electronico = "", telefono = "", activo = True, fecha_creacion = None):
        #Parametros obligatorios
        self.usuario = usuario
        self.clave = clave
        self.tipo_usuario = tipo_usuario
        
        #Parametros opcionales
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.id_creador = id_creador
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.activo = activo
        self.fecha_creacion = fecha_creacion
        
    
    def ingresar(self, usuario, clave):
       bd = Conexion() #Se crea un objeto de la clase Conexion
       
       #Se busca si existe un usuario que coincida con la contraseña introducida
       resultado = bd.execute_query("SELECT usuario, contrasena FROM Usuarios WHERE usuario = ? AND contrasena = ?", [self.usuario, self.clave])
       
       if resultado: # Si existe se establecen los valores
            self.usuario = resultado[0][0]
            self.clave = resultado[0][1]
            return True
       else:
            return False