/*
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/22
*/


INSERT INTO Country(tex_name, tex_iso) VALUES 
 ('British Indian Ocean Territory','IO'),
 ('Honduras','HN'),
 ('Israel','IL'),
 ('India','IN'),
 ('United Kingdom','UK'),
 ('United States of America (USA)','US'),
 ('Uruguay','UY'),
 ('Saint Vincent and the, Grenadines','VC'),
 ('Venezuela','VE')
;


-- Clientes
INSERT INTO User(id_country_fk, tex_firstname, tex_secondname, tex_firstsurname, tex_secondsurname, tex_accessCode) VALUES
 (1, 'Saraann', 'Eula', 'Jull', 'Clewer', 'cli-0001-6zD'),
 (3, 'Joannes', 'Jarvis', 'Ryson', 'Varty', 'cli-0002-0F4'),
 (4, 'Ave', 'Fredia', 'Impson', 'Aicheson', 'cli-0003-1yF'),
 (5, 'Salli', 'Elmore', 'Panchin', 'Nisen', 'cli-0004-RTE'),
 (5, 'Clari', 'Poul', 'Gotling', 'Gouldie', 'cli-0005-2Dh'),
 (5, 'Shelby', 'Latisha', 'Broadberrie', 'Adnett', 'cli-0006-WEo'),
 (6, 'Eduino', 'Corissa', 'Hearne', 'Dosdill,', 'cli-0007-qD2')
;


-- Empleados
INSERT INTO User(id_country_fk, tex_firstname, tex_secondname, tex_firstsurname, tex_secondsurname, bit_type, tex_accessCode) VALUES
 (2, 'Guntar', 'Rubina', 'Kemm', 'Barnewille', 1, 'emp-0008-pyh'),
 (2, 'Deane', 'Kingsley', 'Aish', 'Idenden', 1, 'emp-0009-EOo'),
 (2, 'Beulah', 'Gordy', 'Knagges', 'Mockford',1, 'emp-0010-6lU')
;


INSERT INTO Phonenumber(id_user_fk, tex_prefix, tex_number) VALUES
 (1, '+86', '802 494 1154'),
 (2, '+353', '335 860 5888'),
 (3, '+66', '446 693 8856'),
 (4, '+62', '872 478 5170'),
 (5, '+86', '822 761 6944'),
 (6, '+56', '588 742 7276'),
 (7, '+380', '467 549 1968'),
 (8, '+504', '517 171 0578'),
 (9, '+504', '893 696 8442'),
 (10, '+504', '155 324 4780')
;


INSERT INTO Client(id_user_fk, tex_passport) VALUES
 (1, 'mQsELhIcT7w2'),
 (2, 'uj1D1sK4JFOE'),
 (3, 'ssqSKiyaelZU'),
 (4, 'gIt6FEgJfWBZ'),
 (5, 'f6DcJZdClPG0'),
 (6, 'WZAP0jmXocWA'),
 (7, 'ZjnZrq4v5I5C')
;


-- identicador empleado
INSERT INTO Employee(id_user_fk, dob_salary, tex_hiringDate) VALUES
 (8, 16840.19, '2023-02-27 00:00:00'),
 (9, 10526.36, '2021-05-02 00:00:00'),
 (10, 8434.64, '2020-01-14 00:00:00')
;