/*
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/23
*/


CREATE VIEW vw_getLastId
    AS
        SELECT
            id
        FROM
            User
        ORDER BY 
            id DESC
        LIMIT 1
;