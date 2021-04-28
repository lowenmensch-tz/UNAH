


USE Quiz;

DROP TRIGGER IF EXISTS tg_notificationComment;
DROP TRIGGER IF EXISTS tg_notificationPublication;
DROP TRIGGER IF EXISTS tg_likePublication;

SET @getLastUser = (SELECT id FROM User ORDER BY id DESC LIMIT 1);

DELIMITER $$ 

--
--  Notificación por cada respuesta de usuario a un comentario
--

CREATE TRIGGER  tg_notificationComment 
    AFTER INSERT 
    ON Publication FOR EACH ROW 
BEGIN
        
    IF new.bit_statePublicPrivate = 0 && new.bit_statePublicationComment = 0 -- Comentario público
    THEN 
    -- Insersación
        INSERT INTO NotificationComment(id_publication_fk, id_user_fk) VALUES 
            ( new.id, @getLastUser )
        ;
    END IF;
END $$

--
--  Notificación por cada publicación nueva de un usuario cualquiera
--

CREATE TRIGGER tg_notificationPublication
    AFTER INSERT 
    ON Publication FOR EACH ROW 
BEGIN 

    IF new.bit_statePublicPrivate = 0 -- Publicación (no importa sí esta es pública o privada)
    THEN 
        -- Inserción
        INSERT INTO NotificationPublication(id_publication_fk) VALUES 
            (new.id)
        ;
    END IF ;
END $$


--
-- Like a cualquier publicación o comentario con la condición de que estos sean públicos
--

CREATE TRIGGER tg_likePublication
    AFTER INSERT 
    ON LikePublication FOR EACH ROW 
BEGIN 
    IF (SELECT bit_statePublicPrivate FROM Publication WHERE new.id_publication_fk) = 0 -- Verificar que la publicación sea 'Púbica'
    THEN 

        INSERT INTO LikePublication(id_user_fk, id_publication_fk) VALUES 
            (new.id_user_fk, new.id_publication_fk)
        ;
    END IF ; 
END $$


DELIMITER ;