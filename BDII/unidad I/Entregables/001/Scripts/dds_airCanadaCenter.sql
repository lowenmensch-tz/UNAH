/*
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/22
*/


-- Entidad País, contiene la información de cada país del mundo
CREATE TABLE Country(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    tex_iso VARCHAR(4) NOT NULL, -- El ISO3 es la abreviación internacional estandarizada para cada país
    tex_name VARCHAR(35) NOT NULL UNIQUE -- Nombre del país
);


-- Entidad Usuario
CREATE TABLE User(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_country_fk INTEGER  NOT NULL, -- Definición de Clave foránea, número(s) de teléfono
    tex_firstname TEXT NOT NULL, -- Primer nombre del usuario
    tex_secondname TEXT NOT NULL, -- Segundo nombre del usuario
    tex_firstsurname  TEXT NOT NULL, -- Primer apellido del usuario
    tex_secondsurname  TEXT NOT NULL, -- Segundo apellido del usuario
    bit_type INT2 DEFAULT 0 NOT NULL, -- Tipo de Usuario (0 Cliente | 1 Empleado)
    tex_accessCode VARCHAR(12) UNIQUE NOT NULL, -- Código de acceso al aeropuerto

    FOREIGN KEY (id_country_fk) REFERENCES Country(id)
);


-- Entidad número de teléfono
CREATE TABLE Phonenumber(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_user_fk INTEGER  NOT NULL, -- Definición de Clave foránea que hace referencia a la entidad Usuario, 
    tex_prefix VARCHAR(4) NOT NULL, -- Prefijo del número de país
    tex_number TEXT NOT NULL, -- Número de teléfono

    FOREIGN KEY (id_user_fk) REFERENCES User(id)
);


-- Entidad clientes
CREATE TABLE Client(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_user_fk INTEGER  NOT NULL, -- Definición de Clave foránea que hace referencia a la entidad Usuario, 
    tex_passport VARCHAR(12) NOT NULL UNIQUE, -- Pasaporte, es único y alfanúmerico (acepta letras y números)
    UNIQUE(id_user_fk),
    FOREIGN KEY (id_user_fk) REFERENCES User(id)
);


-- Entidad empleados
CREATE TABLE Employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_user_fk INTEGER  NOT NULL, -- Definición de Clave foránea que hace referencia a la entidad Usuario, 
    -- tex_codEmployee VARCHAR(12) NOT NULL UNIQUE,-- Código del empleado, es único y alfanúmerico (acepta letras y números)
    dob_salary DOUBLE  NOT NULL, -- Salario del empleado
    -- tex_hiringDate TEXT NOT NULL, -- Fecha de contratación, con el siguiente formato: "YYYY-MM-DD HH:MM:SS.SSS" 
    tim_hiringDate DATE DEFAULT (DATETIME('now','localtime')) NOT NULL,

    UNIQUE(id_user_fk),
    FOREIGN KEY (id_user_fk) REFERENCES User(id)
);


-- Bitacora de entrada/salida de personas con acceso al aeropuerto
CREATE TABLE Control(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    bit_type INT2 DEFAULT 0 NOT NULL, -- Tipo de control (0 Salida | 1 Entrada)
    --tex_date TEXT NOT NULL -- Fecha de registro, con el siguiente formato: "YYYY-MM-DD HH:MM:SS.SSS" 
    tim_date DATE DEFAULT (DATETIME('now','localtime')) NOT NULL
);


-- Entidad intersección entre las relaciones Usuario y Control
CREATE TABLE UserControl(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_user_fk INTEGER  NOT NULL, -- Definición de Clave foránea que hace referencia a la entidad Usuario, 
    id_control_fk INTEGER  NOT NULL, -- Definición de Clave foránea que hace referencia a la entidad Control, 

    FOREIGN KEY (id_user_fk) REFERENCES User(id),
    FOREIGN KEY (id_control_fk) REFERENCES Control(id)
);