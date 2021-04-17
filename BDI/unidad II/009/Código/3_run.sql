
USE TriggerProcessing;

/*Caso 1*/
    SET @count = 12;
    CALL sp_createNumbers(@count);
    SELECT * FROM NumbersSquared;
/*
    Cuando desde el diseño/creación del sistema se sabe que es necesario realizar un cálculo, el trigger puede resolver el problema ya que desde la primera inserción se generará el cálculo solicitado.
*/

/*Caso 2*/
    INSERT INTO NumbersSquared(num_id_fk, num_squared)
        SELECT
            id, 
            SQRT(id)
        FROM 
            Numbers
    ;
    SELECT * FROM NumbersSquared_insert;

/*
    Cuando los datos y las tablas ya existen y están pobladas, el trigger no puede tener el efecto requerido en el sistema, ya que el cálculo de los números existirá únicamente para los nuevos registros de la tabla.
*/

/*Caso 3*/
    SELECT * FROM vw_NumbersSquared;
/*
    Cuando se necesita recalcular la raíz cuadrada, cada vez que se solicita la información.
*/