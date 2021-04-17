
USE Example;

DROP VIEW IF EXISTS vw_firstDeviceMeasureRecent;
CREATE VIEW vw_firstDeviceMeasureRecent AS 
    SELECT
        *
    FROM 
        Measure
    WHERE
        device=1
    ORDER BY
        id DESC
    LIMIT 
        1000
;  

SELECT
    "First Device Measure Recent" AS "Vista",
    COUNT(*) AS "Cantidad"
FROM 
    vw_firstDeviceMeasureRecent
;

/*
    1) Una vista que muestre la cantidad de registros por cada mes, para el año 2021, llamada "CountMonth2021"
*/

DROP VIEW IF EXISTS vw_countMonth2021;
CREATE VIEW vw_countMonth2021 AS
    SELECT
        MONTH(Measure.date) AS "Mes",
        COUNT(*) AS "Cantidad" 
    FROM
        Measure 
    WHERE 
        YEAR(Measure.date) = 2021
    GROUP BY
         MONTH(Measure.date)
    ORDER BY 
        MONTH(Measure.date) ASC
;
