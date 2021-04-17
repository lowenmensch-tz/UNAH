
DROP DATABASE IF EXISTS AdvancedSQLProcedures; 
CREATE DATABASE AdvancedSQLProcedures CHARACTER SET utf8;
USE AdvancedSQLProcedures;

    -- Expresiones Regulares
    SET @record = '{"name":"Juan Fernando", "age":"41", "uid":"0801-1980-01012"}';
    SET @pattern = "^0801-?\\d{4}-?\\d{5}$";
    SET @uid = JSON_UNQUOTE(JSON_EXTRACT(@record, "$.uid"));

    SELECT 
        @uid AS "UID",
        CASE 
            WHEN (@uid RLIKE @pattern) = 0 THEN "Falso"
            ELSE "Verdadero"
        END "Cumple con el patrón"
    ;