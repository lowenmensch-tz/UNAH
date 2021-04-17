# -*- coding: utf-8 -*-

"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0
    @date 2021/03/24
"""

class ConfigConnection:

    def __init__(self, host, port, user, password, database): 

        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        