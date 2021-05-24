/*
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/23
*/


CREATE VIEW vw_getLastIdUser
    AS
        SELECT
            id
        FROM
            User
        ORDER BY 
            id DESC
        LIMIT 1
;



CREATE VIEW vw_getLastIdControl
    AS
        SELECT
            id
        FROM
            Control
        ORDER BY 
            id DESC
        LIMIT 1
;

CREATE VIEW vw_binacle
    AS 
        SELECT 
            User.tex_firstname AS name, 
            CASE 
                WHEN Control.bit_type = 0 THEN 'Sale'
                ELSE 'Entra'
            END AS access, 
            CASE 
                WHEN User.bit_type = 0 THEN 'Cliente'
                ELSE 'Empleado'
            END AS type, 
            Control.tim_date AS date
        FROM 
            User 
        INNER JOIN 
            UserControl ON User.id = UserControl.id_user_fk
        INNER JOIN 
            Control ON UserControl.id_control_fk = Control.id
        ORDER BY 
            Control.tim_date DESC
; 