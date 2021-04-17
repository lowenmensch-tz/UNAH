# -*- coding: utf-8 -*-
 
"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/04/14
"""

class ConfigConnection: 

    def __init__(self, host, port, user, password, database): 

        self.host = host  
        self.port = port  
        self.user = user  
        self.password = password  
        self.database = database