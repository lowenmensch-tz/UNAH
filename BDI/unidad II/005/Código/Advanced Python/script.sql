
DROP DATABASE IF EXISTS `Example`; 
CREATE DATABASE `Example` CHARACTER SET utf8;
USE `Example`;

CREATE TABLE `Measure`(
`id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Autoincremental.',
`device` int(11) NOT NULL COMMENT 'Device Id.',
`temperature` decimal(10, 4) DEFAULT NULL COMMENT 'Temperature in celcius.',
`date` timestamp NOT NULL DEFAULT CURRENT_DATE COMMENT 'Date for the temperature.',
PRIMARY KEY(`id`) 
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT = 'Measure Historic Table';