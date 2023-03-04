--CREACION DE LAS TABLAS
CREATE TABLE Usuarios(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tipo_usuario INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    usuario Text NOT NULL UNIQUE,
    contrasena TEXT NOT NULL,
    ID_Creador INTEGER NOT NULL,
    correo_electronico TEXT NOT NULL UNIQUE,
    telefono TEXT NOT NULL,
    activo TEXT NOT NULL,
    fecha_creacion DATE NOT NULL,
    FOREIGN KEY (id_tipo_usuario)
    REFERENCES Tipo_Usuario(id_tipo_usuario),
    FOREIGN KEY (ID_Creador)
    REFERENCES Usuarios(id_usuario)
);

CREATE TABLE Orientacion_Sexual(
    id_orientacion_sexual INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Nacionalidad(
    id_nacionalidad INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Provincia(
    id_provincia INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Sexo(
    id_sexo INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Tipo_Documento(
    id_tipo_documento INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Condiciones_Sujeto(
    id_condiciones_sujeto INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sujeto INTEGER NOT NULL,
    id_condicion_medica INTEGER NOT NULL,
    FOREIGN KEY (id_sujeto)
    REFERENCES Sujetos_estudio(id_sujeto),
    FOREIGN KEY (id_condicion_medica)
    REFERENCES Condiciones_Medicas(id_condicion_medica)
);

CREATE TABLE Condiciones_Medicas(
    id_condicion_medica INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Condicion_Parametro(
    id_condicion_parametro INTEGER PRIMARY KEY AUTOINCREMENT,
    id_condicion_medica INTEGER NOT NULL,
    id_parametro_fisiologico INTEGER NOT NULL,
    FOREIGN KEY (id_condicion_medica)
    REFERENCES Condiciones_Medicas(id_condicion_medica),
    FOREIGN KEY (id_parametro_fisiologico)
    REFERENCES Parametros_fisiologicos(id_parametro_fisiologico)
);

CREATE TABLE Tipo_Usuario(
    id_tipo_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Historico_Solicitud(
    id_historico_solicitud INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    fecha_solicitud DATE NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (id_usuario)
    REFERENCES Usuarios(id_usuario)
    );

CREATE TABLE Mediciones_Sujeto (
    id_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sujeto INTEGER NOT NULL,
    peso_sujeto REAL NOT NULL,
    altura_sujeto REAL NOT NULL,
    fecha_medicion DATETIME NOT NULL,
    FOREIGN KEY (id_sujeto) 
    REFERENCES Sujetos_estudio(id_sujeto)
);

CREATE TABLE Medicion_Parametro (
    id_detalle_medicion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_medicion INTEGER NOT NULL,
    id_parametro_fisiologico INTEGER NOT NULL,
    medida_parametro_fisiologico REAL NOT NULL,
    FOREIGN KEY (id_medicion)
    REFERENCES Mediciones_sujeto(id_medicion),
    FOREIGN KEY (id_parametro_fisiologico)
    REFERENCES Parametros_fisiologicos(id_parametro_fisiologico)
);

CREATE TABLE Parametros_Fisiologicos (
    id_parametro_fisiologico INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE,
    min_estandar REAL NOT NULL,
    max_estandar REAL NOT NULL,
    alerta_bajo REAL,
    alerta_alto REAL,
    critico_bajo REAL,
    critico_alto REAL,
    instrucciones TEXT NOT NULL
);

CREATE TABLE Genero (
    id_genero INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Sujetos_Estudio (
    id_sujeto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    id_tipo_documento INTEGER NOT NULL,
    codigo_documento TEXT NOT NULL,
    id_sexo INTEGER NOT NULL,
    id_genero INTEGER NOT NULL,
    id_orientacion_sexual INTEGER NOT NULL,
    id_nacionalidad INTEGER NOT NULL,
    id_provincia INTEGER NOT NULL,
    correo_electronico TEXT NOT NULL,
    FOREIGN KEY (id_tipo_documento)
    REFERENCES Tipo_documento(id_tipo_documento),
    FOREIGN KEY (id_sexo)
    REFERENCES Sexo(id_sexo),
    FOREIGN KEY (id_genero)
    REFERENCES Genero(id_genero),
    FOREIGN KEY (id_orientacion_sexual)
    REFERENCES Orientacion_sexual(id_orientacion_sexual),
    FOREIGN KEY (id_nacionalidad)
    REFERENCES Nacionalidad(id_nacionalidad),
    FOREIGN KEY (id_provincia)
    REFERENCES Provincia(id_provincia),
    UNIQUE(id_tipo_documento, codigo_documento)
);

-- INSERCION DE LOS DATOS INICIALES