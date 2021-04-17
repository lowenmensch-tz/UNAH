# -*- coding: utf-8 -*-

"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0
    @date 2021/03/24
"""


from ConfigConnection import ConfigConnection
from MySQLEngine import MySQLEngine

#Instancia de configuración
config = ConfigConnection("localhost", "3306", "admin", "admin", "Example")

#Instancia de conexión con la base de datos
engine = MySQLEngine(config)

#Se realiza una consulta de SQL
result = engine.selectPage("SELECT id, device, temperature, date FROM Measure LIMIT 10, 20  ;", 5, 50)

#Se guarda el resultado como un archivo
engine.saveAsTable("Temperature.txt", result, ["id", "device", "temperature", "date"])