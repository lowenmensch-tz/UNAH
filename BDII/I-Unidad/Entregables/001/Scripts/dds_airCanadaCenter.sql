/*
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/22
*/

DROP IF EXISTS AirCanadaCente;
CREATE DATABASE AirCanadaCente;


-- Entidad País, contiene la información de cada país del mundo
CREATE TABLE Country(
    id INTEGER UNSIGNED AUTOINCREMENT NOT NULL PRIMARY KEY, 
    tex_iso VARCHAR(4) NOT NULL UNIQUE, -- El ISO3 es la abreviación internacional estandarizada para cada país
    tex_name VARCHAR(35) NOT NULL UNIQUE -- Nombre del país
);

-- Entidad de los clientes
CREATE TABLE User(
    id INTEGER UNSIGNED AUTOINCREMENT NOT NULL PRIMARY KEY, 
    id_country_fk INTEGER NOT NULL, -- Definición de Clave foránea, número(s) de teléfono
    tex_firstname TEXT NOT NULL, -- Primer nombre del usuario
    tex_secondname TEXT NOT NULL, -- Segundo nombre del usuario
    tex_firstsurname  TEXT NOT NULL, -- Primer apellido del usuario
    tex_secondsurname  TEXT NOT NULL, -- Segundo apellido del usuario
    bit_type INT2 DEFAULT 0 NOT NULL, -- Tipo de Usuario (0 Cliente | 1 Empleado)

    FOREIGN KEY (id_country_fk) REFERENCES Country(id)
);

