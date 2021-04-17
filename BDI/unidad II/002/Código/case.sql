
DROP DATABASE IF EXISTS AdvancedSQLProcedures;
CREATE DATABASE AdvancedSQLProcedures CHARACTER SET utf8;
USE AdvancedSQLProcedures;

    -- Se define una variable con el contenido de un caso de uso
    SET @sampleCategory = "deviceA";

    -- Se aplica un caso de selección
    SELECT 
        CASE 
            WHEN @sampleCategory = "deviceA" THEN "0A1"
            WHEN @sampleCategory = "deviceB" THEN "0B2"
            WHEN @sampleCategory = "deviceC" THEN "0C3"
            ELSE "0UNK"
        END 
        INTO @sampleCategory
    ;

    SELECT @sampleCategory AS "Type of Item";

    -- Se crea una tabla de cola de peticiones
    CREATE TABLE RequestQueue(
        id SERIAL PRIMARY KEY,
        jso_request JSON NOT NULL COMMENT "" ,
        bit_read BIT(1) NOT NULL DEFAULT 0 COMMENT ""
    ) COMMENT "Sample Data";

    INSERT INTO RequestQueue(jso_request, bit_read) VALUES 
        ('{"service":"00f21x2", "user":"bdi", "command":"INBOX"}', 1),
        ('{"service":"00f21x2", "user":"bdi", "command":"TRASH"}', 0)
    ;

    -- Seleccionar el último registro de petición no atendido. Almacenar en un espacio temporal de memoria.
    SET @lastRequest = (SELECT jso_request FROM RequestQueue WHERE bit_read = 0 ORDER BY id ASC LIMIT 1);
    SET @lastCommand = JSON_UNQUOTE( JSON_EXTRACT(@lastRequest, "$.command") ); -- Solución errónea https://mariadb.com/kb/en/json-functions/

    SELECT @lastRequest AS "última petición en Queue" , @lastCommand AS "último comando";

    -- =, LIKE, STRCMP
    SELECT 
        @lastCommand AS "Comando", 
        CASE 
            WHEN @lastCommand = "INBOX" THEN "Solicitud de inbox STMP de la bandeja de correo"
            WHEN @lastCommand = "TRASH" THEN "Solicitud de trash STMP de la bandeja de correo"
            ELSE "Instrucción desconocida"
        END AS "Acción solicitada"
    ;