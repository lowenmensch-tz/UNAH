"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/24
"""

import sqlite3
import os

class SQLiteEngine: 


    def __init__(self) -> None:

        self.database = os.path.join(os.path.dirname(__file__), 'AirCanadaCenter.db')
        self.connection = sqlite3.connect( self.database )
        self.cursor = self.connection.cursor()



    #Insertar datos
    def insert(self, table: str, data: list) -> None: 

        query = 'Insert INTO {} VALUES (?,?,?)'.format( table )
        self.cursor.executemany( query, data )
        self.connection.commit()


    
    #SELECT statments
    def select(self, query: str) -> list: 

        self.cursor.execute(query)
        return self.cursor.fetchall()


    """
        CREATE statements
        Ejecuta varios statements a la vez
    """
    def create(self, query: str) -> None: 

        self.cursor.executescript( query )
        self.close_connection()


    #Cerrar conexión
    def close_connection(self) -> None: 

        self.connection.close()