# -*- coding: utf-8 -*-

import mysql.connector

"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0
    @date 2021/03/24
"""

class MySQLEngine:

    def __init__(self, config):
        self.config = config

        self.mydb = mysql.connector.connect(
            host = self.config.host,
            port = self.config.port,
            user = self.config.user,
            password = self.config.password,
            database = self.config.database
        )

    def select(self, query):
        pass