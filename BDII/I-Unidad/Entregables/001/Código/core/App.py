# -*- coding: utf-8 -*-

from os import access
from core.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMainWindow
from core.SQLiteEngine import SQLiteEngine


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        
        super(App, self).__init__(parent)
        self.setupUi(self)
        
        self.engine = SQLiteEngine()
        
        #self.registerPushButton.clicked.connect( self.verify_access_code )
        self.operDoorPushButton.clicked.connect( self.insert_user_in_control )
        
    
    #Caja de mensajes    
    def message_box(self, title: str, message: str) -> None: 
        
        QMessageBox.about(self, title, message)
    

    # Verifica sí el código ingresado está asociado a un usuario
    def verify_access_code(self) -> None:
        
        self.access_code = (self.idLineEdit.text()).strip()

        try: 
            query = "SELECT COUNT(*) FROM User WHERE tex_accessCode  = '{}'".format(self.access_code)
            response = self.engine.select(query).pop()[0]

            print( self.access_code )
            
            #Existe
            if response: 
                return True
            else: 
                self.message_box("Mensaje", "Código de usuario incorrecto")
                self.idLineEdit.setText("")
                self.idLineEdit.cursor()
                return False

        except IndexError as ie: 
            print("Error al traer dato de la base de datos 'verify_access_code'")

        except sqlite3.OperationalError as sql: 
            print("La base de datos no está disponible")



    #Registra el usuario en la Bitacora
    # (0 Salida | 1 Entrada)
    def insert_user_in_control(self) -> None: 

        if self.verify_access_code(): 
        
            #Entra al aeropuerto
            if self.radioButton.isChecked(): 
                
                self.control(1)
            else: 
                self.control(0)


    #Inserción de los datos en la tabla Control
    def control(self, access_control: int) -> None:

        try:

            #table: parameters, values, data
            self.engine.insert(table="Control", parameters="bit_type", values='(?)', data=(access_control, ))

            id_user = self.engine.select("SELECT id FROM User WHERE tex_accessCode  = '{}'".format(self.access_code)).pop()[0] 
            id_control = self.engine.select("SELECT id FROM vw_getLastIdControl").pop()[0] 

            print( id_user, id_control )
            
            self.engine.insert(table="UserControl", parameters="id_user_fk, id_control_fk", values='(?, ?)', data=(id_user, id_control))

        except IndexError as ie: 
            print("Error al traer dato de la base de datos 'control'")