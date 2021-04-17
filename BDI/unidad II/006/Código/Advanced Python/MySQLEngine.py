# -*- coding: utf-8 -*-

import mysql.connector

"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0
    @date 2021/03/24
"""

# $ sudo -H pip3 install Tabulate
from tabulate import tabulate

#REGEXP
import re


class MySQLEngine:

    def __init__(self, config):
        self.config = config

        self.mydb = mysql.connector.connect(
            host=self.config.host,
            port=self.config.port,
            user=self.config.user,
            password=self.config.password,
            database=self.config.database
        )

        self.link = self.mydb.cursor()

    def select(self, query):
        
        self.link.execute(query)
        return self.link.fetchall()

    def selectPage(self, query, page=0, count=10):

        #Limpiar la query y remover el LIMIT que exista
        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+(,\d+)?\s*;\s*", "", query)

        #Crear nuestro propio componente LIMIT usando los parámetros
        query = "{} LIMIT {},{};".format(query, page, count)

        print(query)

        self.link.execute(query)
        return self.link.fetchall()

    def printIdDeviceTemperatureDate(self, result): 

        for id, device, temperature, date in result: 
            print( "\tRegistro: {},{},{},{}".format(id, device, temperature, date) )

    def printAsTable(self, result, headers=[]):

        if not headers:
            print( tabulate(result) )
        else:
            print( tabulate(result, headers=headers) )


    def saveAsTable(self, fileName, result, headers=[]):

        content = ""

        if not headers:
            content = tabulate(result)
        else: 
            content = tabulate(result, headers=headers)

        f=open(fileName, "w")
        f.write("\n\n{}\n\n".format(content))
        f.close()

        return True