
USE TriggerProcessing;

DROP TRIGGER IF EXISTS tg_calculateSquareRoot;

DELIMITER $$

CREATE TRIGGER tg_calculateSquareRoot
    AFTER INSERT 
    ON Numbers FOR EACH ROW
BEGIN 
    INSERT INTO NumbersSquared(num_id_fk, num_squared) VALUES
        (new.id, SQRT(new.id)) 
    ;
END $$

DELIMITER ;