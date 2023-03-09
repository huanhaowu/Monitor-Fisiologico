--CREACION DE LAS TABLAS
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

CREATE TABLE Condiciones_Medicas(
    id_condicion_medica INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL UNIQUE
);

CREATE TABLE Tipo_Usuario(
    id_tipo_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
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
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
    id_medicion INTEGER NOT NULL,
    id_parametro_fisiologico INTEGER NOT NULL,
    medida_parametro_fisiologico REAL NOT NULL,
    PRIMARY KEY(id_medicion, id_parametro_fisiologico),
    FOREIGN KEY (id_medicion)
    REFERENCES Mediciones_sujeto(id_medicion),
    FOREIGN KEY (id_parametro_fisiologico)
    REFERENCES Parametros_fisiologicos(id_parametro_fisiologico)
);

CREATE TABLE Condiciones_Sujeto(
    id_sujeto INTEGER NOT NULL,
    id_condicion_medica INTEGER NOT NULL,
    PRIMARY KEY(id_sujeto, id_condicion_medica),
    FOREIGN KEY (id_sujeto)
    REFERENCES Sujetos_estudio(id_sujeto),
    FOREIGN KEY (id_condicion_medica)
    REFERENCES Condiciones_Medicas(id_condicion_medica)
);

CREATE TABLE Condicion_Parametro(
    id_condicion_medica INTEGER NOT NULL,
    id_parametro_fisiologico INTEGER NOT NULL,
    PRIMARY KEY(id_condicion_medica, id_parametro_fisiologico),
    FOREIGN KEY (id_condicion_medica)
    REFERENCES Condiciones_Medicas(id_condicion_medica),
    FOREIGN KEY (id_parametro_fisiologico)
    REFERENCES Parametros_fisiologicos(id_parametro_fisiologico)
);

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

CREATE TABLE Historico_Solicitud(
    id_historico_solicitud INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    fecha_solicitud DATE NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (id_usuario)
    REFERENCES Usuarios(id_usuario)
);
-- INSERCION DE LOS DATOS INICIALES
-- Tipo_Usuario
INSERT INTO Tipo_Usuario (descripcion) VALUES ('Administrador');
INSERT INTO Tipo_Usuario (descripcion) VALUES ('Analista');

-- Parametros_Fisiologicos
INSERT INTO Parametros_Fisiologicos (descripcion, min_estandar, max_estandar, alerta_bajo, alerta_alto, critico_bajo, critico_alto, instrucciones) 
VALUES 
('Temperatura', 36, 37, 34, 40, 29.99, 46, '\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3'), 
('Presion Arterial Sistolica', 110, 120, 90, 139, 70, NULL, '\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3'), 
('Presion Arterial Diastolica', 70, 80, 60, 89, 50, NULL, '\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3'), 
('Frecuencia Cardiaca', 60, 100, 40, 149, 34.99, NULL, '\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3'), 
('Saturacion de Oxigeno', 95, 100, 89, NULL, 0, NULL, '\n\t\t\t INSTRUCCIONES: \n 1) Paso 1 \n 2) Paso 2 \n 3) Paso 3');

-- Genero
INSERT INTO Genero (descripcion) VALUES ('Hombre');
INSERT INTO Genero (descripcion) VALUES ('Mujer');
INSERT INTO Genero (descripcion) VALUES ('No Binario');
INSERT INTO Genero (descripcion) VALUES ('Transgenero');
INSERT INTO Genero (descripcion) VALUES ('Genero fluido');
INSERT INTO Genero (descripcion) VALUES ('Otro');



-- Orientacion_Sexual
INSERT INTO Orientacion_Sexual (descripcion) VALUES ('Heterosexual');
INSERT INTO Orientacion_Sexual (descripcion) VALUES ('Homosexual');
INSERT INTO Orientacion_Sexual (descripcion) VALUES ('Bisexual');
INSERT INTO Orientacion_Sexual (descripcion) VALUES ('Pansexual');
INSERT INTO Orientacion_Sexual (descripcion) VALUES ('Otro');

-- Nacionalidad
INSERT INTO Nacionalidad (descripcion) VALUES ('Dominicana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Argentina');
INSERT INTO Nacionalidad (descripcion) VALUES ('Boliviana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Brasilena');
INSERT INTO Nacionalidad (descripcion) VALUES ('Chilena');
INSERT INTO Nacionalidad (descripcion) VALUES ('Colombiana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Ecuatoriana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Paraguaya');
INSERT INTO Nacionalidad (descripcion) VALUES ('Peruana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Uruguaya');
INSERT INTO Nacionalidad (descripcion) VALUES ('Venezolana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Mexicana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Cubana');
INSERT INTO Nacionalidad (descripcion) VALUES ('Estadounidense');
INSERT INTO Nacionalidad (descripcion) VALUES ('Canadiense');
INSERT INTO Nacionalidad (descripcion) VALUES ('Otro');

-- Provincia
INSERT INTO Provincia (descripcion) VALUES ('Santo Domingo');
INSERT INTO Provincia (descripcion) VALUES ('Azua');
INSERT INTO Provincia (descripcion) VALUES ('Bahoruco');
INSERT INTO Provincia (descripcion) VALUES ('Barahona');
INSERT INTO Provincia (descripcion) VALUES ('Dajabon');
INSERT INTO Provincia (descripcion) VALUES ('Distrito Nacional');
INSERT INTO Provincia (descripcion) VALUES ('Duarte');
INSERT INTO Provincia (descripcion) VALUES ('Elias Piña');
INSERT INTO Provincia (descripcion) VALUES ('El Seibo');
INSERT INTO Provincia (descripcion) VALUES ('Espaillat');
INSERT INTO Provincia (descripcion) VALUES ('Hato Mayor');
INSERT INTO Provincia (descripcion) VALUES ('Hermanas Mirabal');
INSERT INTO Provincia (descripcion) VALUES ('Independencia');
INSERT INTO Provincia (descripcion) VALUES ('La Altagracia');
INSERT INTO Provincia (descripcion) VALUES ('La Romana');
INSERT INTO Provincia (descripcion) VALUES ('La Vega');
INSERT INTO Provincia (descripcion) VALUES ('Maria Trinidad Sanchez');
INSERT INTO Provincia (descripcion) VALUES ('Monseñor Nouel');
INSERT INTO Provincia (descripcion) VALUES ('Monte Cristi');
INSERT INTO Provincia (descripcion) VALUES ('Monte Plata');
INSERT INTO Provincia (descripcion) VALUES ('Pedernales');
INSERT INTO Provincia (descripcion) VALUES ('Peravia');
INSERT INTO Provincia (descripcion) VALUES ('Puerto Plata');
INSERT INTO Provincia (descripcion) VALUES ('Samana');
INSERT INTO Provincia (descripcion) VALUES ('San Cristobal');
INSERT INTO Provincia (descripcion) VALUES ('San Jose de Ocoa');
INSERT INTO Provincia (descripcion) VALUES ('San Juan');
INSERT INTO Provincia (descripcion) VALUES ('San Pedro de Macoris');
INSERT INTO Provincia (descripcion) VALUES ('Sanchez Ramirez');
INSERT INTO Provincia (descripcion) VALUES ('Santiago');
INSERT INTO Provincia (descripcion) VALUES ('Santiago Rodriguez');
INSERT INTO Provincia (descripcion) VALUES ('Valverde');

-- Tipo_Documento
INSERT INTO Tipo_Documento (descripcion) VALUES ('Cedula');
INSERT INTO Tipo_Documento (descripcion) VALUES ('Pasaporte');

-- Sexo
INSERT INTO Sexo (descripcion) VALUES ('Masculino');
INSERT INTO Sexo (descripcion) VALUES ('Femenino');
INSERT INTO Sexo (descripcion) VALUES ('Intersexual');

-- Condiciones_Medicas
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Anemia');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Hipertiroidismo');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Hipotiroidismo');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Diabetes');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Sobrepeso');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Asma');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Hipertension');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Hipotension');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Migrana');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Enfermedad Pulmonar Obstructiva Cronica');
INSERT INTO Condiciones_Medicas (descripcion) VALUES ('Insuficiencia Cardiaca');

-- Condicion_Parametro
INSERT INTO Condicion_Parametro (id_parametro_fisiologico, id_condicion_medica) 
VALUES 
(1, 3), (1, 6),
(2, 1), (2, 2), (2, 3), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 14),
(3, 1), (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 14),
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 10), (4, 11), (4, 12), (4, 14),
(5, 2), (5, 4), (5, 8), (5, 9), (5, 10), (5, 11), (5, 13), (5, 14)