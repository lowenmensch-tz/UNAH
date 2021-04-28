# -*- coding: utf-8 -*-
 
import mysql.connector

"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/04/16
"""

from tabulate import tabulate
import re

class MySQLEngine: 

    def __init__(self, config): 

        self.config = config
        self.mydb = mysql.connector.connect(
            host= self.config.host, 
            port= self.config.port, 
            user= self.config.user, 
            password= self.config.password, 
            database= self.config.database 
        )

        self.link = self.mydb.cursor()

        #Número de ejecución de la cláusula SELECT
        self.countExecuteSelect = 0
        #Número de ejecución del DDS
        self.countExecuteDDS = 0
        #Número de ejecución del DMS
        self.countExecuteDMS = 0

    #Clausula SELECT
    def select(self, query, headers=[], page=0, count=10): 


        #Limpiar la query y remover el LIMIT que exista
        query = re.sub(r"\s+([Ll][Ii][Mm][Ii][Tt]\s+\d+(,\d+)?)?\s*;?\s*$", "", query)

        #Crear nuestro propio componente LIMIT usando los parámetros
        query = "{} LIMIT {}, {};".format(query, page, count)

        result = self.link.execute(query)

        #Muestra en pantalla el resultado de la consulta
        print(  tabulate(result, headers) )

        self.count += 1
        #return self.link.fetchall()


    #Ejecuta instrucciones no fetch
    #Realiza inserciones de tuplas a la base de datos
    def dms(self, table, fields=[], values=[]): 

        query = "INSERT INTO {} ({}) VALUES ({});".format( table, ", ".join(fields), self.prepareQuery(values) )

        print( query )

        result = self.link.execute(query)
        self.mydb.commit()

        self.countExecuteDMS += 1
        print("Se ha ejecutado la transacción '{}', con el resultado {}\\nN de ejecución: {}".format(
                    query, 
                    result, 
                    self.countExecuteDMS
                )
            )

    def ddsDms(self, query): 

        result = self.link.execute(query)
        print("Se ha ejecutado la transacción '{}', con el resultado {}".format(query, result))
        return result



    #Ejecuta la definición de la base de datos
    def dds(self, query): 

        result = self.link.execute(query)

        self.countExecuteDDS += 1
        print("Se ha ejecutado la transacción '{}', con el resultado {}, N de ejecución {}".format(
                    query, 
                    result, 
                    self.countExecuteDDS
                )
            )
        

     #Agrega comillas para los n valores de los campos de un query
    def prepareQuery(self, values):
        
        data = ""

        for value in values: 

            #Evita colocar comillas simples a los tipo de dato entero
            if type(value) == int:  
                data += "{} ".format(value)
            else: 
                data += "'{}' ".format(value)

        data = data.replace(" ", ",")
        data = re.sub(r",$", "", data)

        return data