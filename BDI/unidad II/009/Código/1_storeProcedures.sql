
USE TriggerProcessing; 

DROP PROCEDURE IF EXISTS sp_createNumbers;

DELIMITER $$

CREATE PROCEDURE sp_createNumbers(IN COUNT INT)
BEGIN
    SET @counter = 0;
    WHILE (@counter <= COUNT) DO
        INSERT INTO Numbers() VALUES ();
        SET @counter = @counter + 1 ;
    END WHILE;
END $$

DELIMITER ;