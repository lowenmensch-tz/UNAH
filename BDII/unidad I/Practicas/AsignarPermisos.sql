/*
	@author kenneth.cruz@unah.hn
	@version 0.1.0
	@date 2021/05/31
*/

-- Crear base de datos 
---------------------------------------
CREATE DATABASE TestUserInDatabase;
USE TestUserInDatabase;
---------------------------------------


-- Crear usuario
---------------------------------------
CREATE LOGIN neonfoo
WITH PASSWORD = 'dsA421#$$$#Klm';  
CREATE USER neonfoo FOR LOGIN neonfoo;
---------------------------------------


-- Asignar usuario a base de datos
---------------------------------------
ALTER USER neonfoo
WITH 
DEFAULT_SCHEMA = TestUserInDatabase;
---------------------------------------


-- Crear una tabla
---------------------------------------
CREATE TABLE test(
	id INT IDENTITY(1, 1) PRIMARY KEY, 
	tex_firstName TEXT NOT NULL, 
	tex_lastName TEXT NOT NULL,
	tim_time DATETIME NOT NULL DEFAULT GETDATE(), 
	nva_json NVARCHAR(MAX) NOT NULL
);
---------------------------------------


-- Asignar accesos para crear tabla
---------------------------------------
USE TestUserInDatabase;
GRANT CREATE TABLE TO neonfoo;
---------------------------------------


-- Asignar privilegios all
---------------------------------------
GRANT ALL PRIVILEGES TO neonfoo;
---------------------------------------


-- Revocar privilegios all
---------------------------------------
REVOKE ALL PRIVILEGES TO neonfoo;
---------------------------------------


-- Asignar accesos para crear tablas accesos totales ya que es el owner de la tabla
---------------------------------------
USE TestUserInDatabase;
GRANT CONTROL ON DATABASE::TestUserInDatabase TO neonfoo;
---------------------------------------


-- Asignar accesos para insertar
---------------------------------------
USE TestUserInDatabase;
GRANT INSERT TABLE TO neonfoo;
---------------------------------------

-- Asignar accesos para update
---------------------------------------
USE TestUserInDatabase;
GRANT UPDATE TABLE TO neonfoo;
---------------------------------------


-- Asignar accesos para delete---------------------------------------
USE TestUserInDatabase;
GRANT DELETE TABLE TO neonfoo;
---------------------------------------


-- Lectura sugerida
-- https://docs.microsoft.com/es-es/sql/t-sql/statements/grant-database-permissions-transact-sql?view=sql-server-ver15