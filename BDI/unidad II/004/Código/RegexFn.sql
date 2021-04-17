
DROP DATABASE IF EXISTS AdvancedSQLProcedures; 
CREATE DATABASE AdvancedSQLProcedures CHARACTER SET utf8;
USE AdvancedSQLProcedures;

    -- Contexto: estudiantes de Excelencia Académica

    CREATE TABLE Student(
        id SERIAL PRIMARY KEY, 
        jso_record JSON NOT NULL COMMENT "Documento con name, age, uid"
    ) COMMENT "Estudiantes de excelencia académica";

    INSERT INTO Student(jso_record) VALUES
        ('{"name":"Pedro García", "age":20 , "uid":"0301200112312"}'),
        ('{"name":"Juan López", "age":21 , "uid":"0501000001234"}'),
        ('{"name":"María Ala", "age":20 , "uid":"1203000012341"}'),
        ('{"name":"Alejandro Lara", "age":21 , "uid":"1803200012341"}'),
        ('{"name":"Alejandro Almendarez", "age":20 , "uid":"0802199999999"}'),
        ('{"name":"Erick López", "age":19 , "uid":"0102199912341"}')
    ;


    /*
        Se desea hacer un recorrido por ciertos departamentos del país, para convencer a estudiantes a que
        realicen sus estudios en STEM (Science, Technology, Engineering and Mathematics), y para ello se 
        requiere el apoyo de estudiantes de excelencia académica cuya procedencia es de dichos departamentos.

        Recorrido 1: Atlántida (01), El Paraíso (07), Francisco Morazán (08) y Yoro (18).
        Recorrido 2: La Paz (12), Comayagua (03) y Cortés (05).

    */

    DELIMITER $$ 
        CREATE FUNCTION fn_jsonName(jso_field JSON) RETURNS TEXT
        BEGIN 
            
                RETURN JSON_UNQUOTE(JSON_EXTRACT(jso_field, "$.name"));

        END $$
        CREATE FUNCTION fn_jsonUID(jso_field JSON) RETURNS TEXT
        BEGIN 

                RETURN JSON_UNQUOTE(JSON_EXTRACT(jso_field, "$.uid"));

        END $$
    DELIMITER ;


    SELECT
        fn_jsonName(jso_record) AS "Nombre del estudiante",

        CASE 
            WHEN fn_jsonUID(jso_record) REGEXP "^((0[178])|(18))\\d{11}$" THEN "Recorrido 1" 
            WHEN fn_jsonUID(jso_record) REGEXP "^((0[35])|(12))\\d{11}$" THEN "Recorrido 2" 
        END AS "Recorrido"
    FROM
        Student
    WHERE
        fn_jsonUID(jso_record) REGEXP "^((0[13578])|(1[28]))\\d{11}$"
    ORDER BY 
        CASE 
            WHEN fn_jsonUID(jso_record) REGEXP "^((0[178])|(18))\\d{11}$" THEN "Recorrido 1" 
            WHEN fn_jsonUID(jso_record) REGEXP "^((0[35])|(12))\\d{11}$" THEN "Recorrido 2" 
        END ASC
    ;

    -- fn_jsonUID(jso_record) REGEXP "^((01)|(07)|(08)|(18)|(12)|(03)|(05))\\\d{11}$"