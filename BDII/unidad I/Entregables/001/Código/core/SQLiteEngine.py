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



    """
        Insertar datos
        parameters ->  (tex_something)
        values -> (?, ?)
        data -> ("C", 1972)
        data -> lang_list = [("Fortran", 1957),("Python", 1991),("Go", 2009),] executemany()
    """
    def insert(self, table: str, parameters: str, values: str, data: list) -> None: 

        query = 'INSERT INTO {} ({}) VALUES {}'.format( table, parameters, values )
        self.cursor.execute( query, data )
        self.connection.commit()
        print("Done insert")        

    
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
        print("Done create")


    #Cerrar conexión
    def close_connection(self) -> None: 

        self.connection.close()