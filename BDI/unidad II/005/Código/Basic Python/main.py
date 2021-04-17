# -*- coding: utf-8 -*-

import mysql.connector

"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0
    @date 2021/03/24
"""

#Generar una conexión
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="admin",
    password="admin",
    database="Example"
)

#imprime el objeto de conexión sptrinf
print("Versión texto del objeto de conexión a MySQL: {}".format(mydb))

#Se crea un cursor de Python como un enlace para crear transacciones de SQL.
link = mydb.cursor()

#Se crea una transacción de selección de datos
link.execute("SELECT id, device, temperature, date FROM Measure LIMIT 10;")
result = link.fetchall()

#Se reconocen e imprimen los resultados
for id, device, temperature, date in result: 
    print("\tRegistro: {},{},{},{}".format(id, device, temperature, date))
```

**Nota** El estudiante deberá experimentar con el resto de transacciones de SQL estudiadas en clase, las cuales hace so del mismo principio antes mostrado.
