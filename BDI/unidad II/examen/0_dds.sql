DROP DATABASE IF EXISTS Quiz;
    CREATE DATABASE Quiz CHARACTER SET utf8;
    USE Quiz;
    
    CREATE TABLE User(
            id SERIAL PRIMARY KEY, 
            tex_email VARCHAR(30) NOT NULL UNIQUE COMMENT "Correo electrónico del usuario", 
            tex_password TEXT NOT NULL COMMENT "Contraseña para ingresar al sistema", 
            tex_nickname TEXT NOT NULL COMMENT "Contraseña para ingresar al sistema"
        )COMMENT = "Entidad usuarios que mantiene el registro de usuarios para el sistema";
    
    
    CREATE TABLE Publication(
            id SERIAL PRIMARY KEY, 
            id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia user", 
            date TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Fecha en la que se realizó la publicación", 
            jso_publication JSON NOT NULL COMMENT "Contiene la información general de la publicación",
            bit_statePublicationComment BIT(1) DEFAULT 0 NOT NULL COMMENT "0 públicación | 1 comentario",
            bit_statePublicPrivate BIT(1) DEFAULT 0 NOT NULL COMMENT "0 público | 1 privado",
            
            FOREIGN KEY (id_user_fk) REFERENCES User(id)
        )COMMENT = "Publicaciones realizadas por un usuario";
    
    
    CREATE TABLE LikePublication(
            id SERIAL PRIMARY KEY, 
            id_user_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad User", 
            id_publication_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Publication", 
            
            FOREIGN KEY (id_user_fk) REFERENCES User(id),
            FOREIGN KEY (id_publication_fk) REFERENCES Publication(id)
        )COMMENT = "Cantidad de like por publicación";
    
    
    CREATE TABLE NotificationComment(
            id SERIAL PRIMARY KEY, 
            id_publication_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Publication", 
            date TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Fecha en la que sucedió la notificación", 
                
            FOREIGN KEY (id_publication_fk) REFERENCES Publication(id)
        )COMMENT = "Notificación por cada comentario en respuesta a una publicación";

    
    CREATE TABLE NotificationPublication(
            id SERIAL PRIMARY KEY, 
            id_publication_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Publication", 
            date TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Fecha en la que sucedió la notificación", 

            FOREIGN KEY (id_publication_fk) REFERENCES Publication(id)
        ) COMMENT = "Notificaciones por cada nueva publicación";


    CREATE TABLE Page(
            id SERIAL PRIMARY KEY, 
            id_publication_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia la entidad Publication", 
            
            FOREIGN KEY (id_publication_fk) REFERENCES Publication(id)
        )COMMENT = "Pagina asociada a la publicación realizada por un usuario";


    CREATE VIEW vw_Notification AS 
        SELECT 
            User.tex_nickname AS "Usuario",
            JSON_UNQUOTE( JSON_EXTRACT(Publication.jso_publication, "$.text") ) AS "Respuesta"
        FROM 
            Notification
        INNER JOIN Publication 
            ON NotificationComment.id_publication_fk = Publication.id
        INNER JOIN User
            ON  Publication.id_user_fk = User.id
    ; 

    /*
        '{"message":"", "image":""}'
    */