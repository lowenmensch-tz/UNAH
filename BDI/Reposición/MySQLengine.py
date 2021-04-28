# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import re

"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/04/28
"""

class MySQLEngine: 

    """
        Constructor de la clase
    """
    def __init__(self, config): 
        self.mydb = mysql.connector.connect(
            host = config.host, 
            port = config.port, 
            user = config.user,
            password = config.password
        )

        self.link = self.mydb.cursor()

        print(  
            "La conexión ha sido: {}".format(
                    "Satisfactoria" 
                    if self.mydb.is_connected() 
                    else "Fallida"
            ) )

    """
        Creación de la base de datos
    """
    def createDatabase(self, dbName): 
        
        try:

            self.link.execute(
                "DROP DATABASE IF EXISTS {}".format(dbName))

            self.link.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(dbName))

            print("Query OK created: {}".format(dbName))

        except mysql.connector.Error as err:

            print("Failed creating database: {}".format(err))
            

    def useDB(self, dbName): 
        
        self.link.execute( "USE {}".format( dbName ) )
        print("Query OK USE: {}".format(dbName))


    """
        Creación de:
            - tablas
            - funciones
            - triggers
            - procedimientos almacenados
        @SENTENCE es un diccionario que contiene la definición de 
        cualquiera de las cláusulas anteriores, puede contener una o varias definiciones
    """
    def createSentence(self, SENTENCE): 
        
        #Diccionario con múltiples operaciones CREATE
        if type(SENTENCE) == dict:

            for sentenceName in SENTENCE:
                
                query = SENTENCE[sentenceName]

                self.create( query )
        
        #Query con la definición de una operación CREATE
        else: 

            self.create( SENTENCE )

            
    """
        Ejecución de cualquier operación enviando directamente el QUERY a través
        del parámetro @query
    """
    def create(self, query): 

        #nombre de la operación (VIEW, FUNCTION, TRIGGER...)
        operation = re.search(r"\s*CREATE [A-Za-z]+", query) 
        operation = (operation.group(0).replace("CREATE", "")).strip()

        #Nombre al que hace referencia esa operación fn_getSomething
        sentenceName = re.search(r"\s*CREATE [A-Za-z]+ [A-Za-z_]+", query) 
        sentenceName = (sentenceName.group(0).split()[-1]).strip()
    
        try:
            self.link.execute( "DROP {} IF EXISTS {};".format(operation, sentenceName) )

            print("Creating {} {}: ".format( operation.lower(), sentenceName), end='')
            self.link.execute(query)

        except mysql.connector.Error as err:
            
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("Query OK created: {}".format(sentenceName))


    """
        Clausula INSERT de los datos
    """
    def insertData(self, query, values=()):
        
        if values: 
            self.link.execute(query, values)
        else: 
            self.link.execute(query)

        self.mydb.commit()
        print("Query OK insert data")

    """
        Ejecuta clausulas SELECT con cierto limite de 'filas' mediante el parametro @size
    """
    def selectHeadRows(self, query, size=None):

        self.link.execute(query)

        if size: 
            return self.link.fetchmany(size=size)
        else: 
            return self.link.fetchall()

    """
        SELECT implementando paginador
    """
    def selectPage(self, query: str, page=0, count=10): 

        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+([, ]\d+)?\s*;\s*", "", query)

        query = ("{} LIMIT {},{};".format(query, page, count))

        self.link.execute(query)
        content = self.link.fetchall()

    def closeConnection(self): 

        self.mydb.close()
        print("Query OK close connection")