# -*- coding:utf-8 -*-

from core.ConfigConnection import ConfigConnection
from core.MySQLEngine import MySQLEngine

#Archivo de configuración
config = ConfigConnection(
                host="localhost", 
                port="3306", 
                user="admin", 
                password="admin", 
                database="Example"
        )

#Instancia de conexión con la base de datos
engine = MySQLEngine(config=config)

#Se realiza una consulta SQL
result = engine.select(query= """
        SELECT 
            "First Device Measure Recent" AS "Vista",
            COUNT(*) AS "Cantidad"
        FROM 
            vw_firstDeviceMeasureRecent
        ;
        """)

#Se imprimen los resultados
engine.printAsTable(result=result, headers=["Vista", "Cantidad"])



#Se realiza una consulta SQL
result = engine.selectPage(query="""
    SELECT
        Mes, Cantidad
    FROM 
        vw_countMonth2021
    ;
""")

#Se imprimen los resultados
engine.printAsTable(result, ["Mes", "Cantidad"])