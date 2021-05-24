'''
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/22
'''

import string
from random import choice


class AccessCode:

    
    def __init__(self) -> None:
        pass


    #Formación del pasaporte
    def generate_passport(self, length_word=12) -> list:

        alphanumeric = string.ascii_letters + string.digits
        return  "".join( [  choice(alphanumeric)  for x in range(length_word) ]) 


    #agrega uno o varios ceros delante del id del empleado
    def user_code(self, id_employee: int) -> str: 

        return "{}{}".format(
            "".join(
                [
                    '0'
                    for x in range( abs(len(str(id_employee))-4) )
                ]
            ), 
            id_employee
        )


    #Formación del código de acceso
    def generate_access_code(self, id_user: int, type_user: str) -> str:

        employee = '{}-{}-'.format("cli" if type_user == 0 else "emp", self.user_code(id_user) )
        return employee + self.generate_passport(length_word=3)



    """
        Tipo de usuario: 
            - 0: cliente
            - 1: empleado
    """
    def example(self):
        
        [print( "User code: {}".format(self.generate_access_code(id_user=x+1, type_user=0)) ) for x in range(7)]
        [print( "User code: {}".format(self.generate_access_code(id_user=x+1, type_user=1)) ) for x in range(7, 10)]