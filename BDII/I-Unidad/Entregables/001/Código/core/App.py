# -*- coding: utf-8 -*-

import re
import string
import sqlite3
from os import access, terminal_size
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from core.GenerateCode import AccessCode
from core.MainWindow import Ui_MainWindow
from core.SQLiteEngine import SQLiteEngine
from PyQt5.QtWidgets import QTreeWidgetItem


class App(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        
        super(App, self).__init__(parent)
        self.setupUi(self)
        
        self.engine = SQLiteEngine()
        self.phonenumber = {}
        self.count = 0
        
        #self.registerPushButton.clicked.connect( self.verify_access_code )
        self.operDoorPushButton.clicked.connect( self.insert_user_in_control )
        self.tabWidget.currentChanged.connect( self.add_country_combo_box )
        self.tabWidget.currentChanged.connect( self.data_visualization )
        
        #self.tabWidget.currentChanged.connect( self.user_register )

        self.addPushButton.clicked.connect( self.phone_register )
        self.registerPushButton.clicked.connect( self.user_register )
        self.deletePushButton.clicked.connect( self.delete_phonenumber )


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
                self.idLineEdit.setFocus()
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

            self.message_box(title="Mensaje", message="Se ha agregado con éxito")
            self.idLineEdit.setText("")

        except IndexError as ie: 
            print("Error al traer dato de la base de datos 'control'")


    """
        Visualización de la bitácora en el QTreewidget
         [('Clari', 'Entra', '2021-05-24 04:58:53')]
    """
    def data_visualization(self) -> None: 
        
        try: 

            #Control
            if self.tabWidget.currentIndex() == 3: 
                query = "SELECT name, access, type, date FROM vw_binacle"
                transaction = self.engine.select(query)
                print( transaction )

                items = []

                self.treeWidget.clear()

                for row in transaction:
                    items.append( QTreeWidgetItem([row[0], row[1], row[2], row[3]]) )

                self.treeWidget.insertTopLevelItems(0, items)
                self.treeWidget.show()

        except IndexError as ie: 
            print("Error al traer dato de la base de datos 'verify_access_code'")



    """
        Registro de los usuarios
    """
    def user_register(self):
        
        self.add_country_combo_box()

        """
        self.lastnamesLineEdit
        self.passportLineEdit
        self.employeeCheckBox
        self.countryComboBox
        self.salaryLineEdit
        self.hiringDateEdit
        self.namesLineEdit
        """
        #Registro de usuario
        if self.tabWidget.currentIndex() == 1: 
            
            if self.validate_personal_date(): 

                access_code = ""
                country = str(self.countryComboBox.currentText()).strip()
                name = ((self.namesLineEdit.text()).strip()).split(" ")
                lastname = ((self.lastnamesLineEdit.text()).strip()).split(" ")

                #Cliente
                if self.validate_client(): 
                    access_code = (AccessCode()).generate_access_code(id_user=self.get_last_id_user(), type_user=0)
                    passport = (self.passportLineEdit.text()).strip()

                    self.execute_insert_data_user(
                                                    access_code, 
                                                    country, name, lastname, 
                                                    table="Client", 
                                                    parameters="id_user_fk, tex_passport", 
                                                    data_parameter=passport
                                                )

                    """                    
                    self.engine.insert(
                            table="Employee", 
                            parameters="id_user_fk, tex_passport", 
                            values='(?, ?)', 
                            data=(
                                    self.get_last_id_user(),
                                    passport     
                            )
                        )
                    
                    self.success(access_code, name[0], lastname[0])
                    """                    

                #Empleado
                elif self.validate_employee(): 
                    
                    access_code = (AccessCode()).generate_access_code(id_user=self.get_last_id_user(), type_user=1)
                    salary = float((self.salaryLineEdit.text()).strip())

                    #table: str, parameters: str, data_parameter
                    self.execute_insert_data_user(
                                                access_code, 
                                                country, name, lastname, 
                                                table="Employee", 
                                                parameters="id_user_fk, dob_salary", 
                                                data_parameter=salary     
                                            )

                    """
                    self.engine.insert(
                            table="Employee", 
                            parameters="id_user_fk, dob_salary", 
                            values='(?, ?)', 
                            data=(
                                    self.get_last_id_user(),
                                    salary     
                            )
                        )
                    
                    self.success(access_code, name[0], lastname[0])
                    """

    

    """
        Inserta los datos para la tabla 'User'
    """
    def execute_insert_data_user(self, access_code: str ,country: str ,name: list ,lastname: list, table: str, parameters: str, data_parameter): 
        
        try:
        
            self.engine.insert(
                            table="User", 
                            parameters="id_country_fk, tex_firstname, tex_secondname, tex_firstsurname, tex_secondsurname, bit_type, tex_accessCode", 
                            values='(?, ?, ?, ?, ?, ?, ?)', 
                            data=(
                                    self.get_country(country), name[0], name[1], 
                                    lastname[0], lastname[1], 1, access_code
                                )
                        )

            if len(self.phonenumber): 
                [
                    self.engine.insert(
                            table="Phonenumber", 
                            parameters="id_user_fk, tex_prefix, tex_number",
                            values='(?, ?, ?)',
                            data=(
                                self.get_last_id_user(),
                                phonenumber[0], 
                                phonenumber[1] 
                            )
                        )
                    
                    for k, phonenumber in self.phonenumber.items()
                ]

            self.engine.insert(
                    table=table, 
                    parameters=parameters, 
                    values='(?, ?)', 
                    data=(
                            self.get_last_id_user(),
                            data_parameter     
                    )
                )
            
            self.success(access_code, name[0], lastname[0])
            self.clean_register_user_screen()

        except sqlite3.OperationalError as soe: 
            print("Algún error en la ejecución del insert: {}".format(soe))


    """
        Mensaje de éxito sobre el ingreso
        de los datos en la base de datos
    """
    def success(self, access_code: str, name: str, lastname: str) ->  None: 

        self.message_box(title="Mensaje", message="El usuario: {} Se ha agregado con éxito".format(name + ' ' + lastname))
        self.message_box(title="Mensaje", message="Su código de acceso es: {}".format(access_code))


    """ 
        Validación de:
        1. Nombres
        2. Apellidos
        3. País
    """
    def validate_personal_date(self) -> bool: 
        
        name = ((self.namesLineEdit.text()).strip()).split(" ")
        lastname = ((self.lastnamesLineEdit.text()).strip()).split(" ")
        country = str(self.countryComboBox.currentText()).strip()

        if name[0] == "" or len(name) < 2: 
            self.message_box(title="Atención", message="Revise el Formato:\n1. Nombre vacío\nEs necesario ingresar dos nombres")
            self.namesLineEdit.setFocus()
            return False
        elif lastname[0] == "" or len(lastname) < 2: 
            self.message_box(title="Atención", message="Revise el Formato:\n1. Apellido vacío\nEs necesario ingresar dos apellidos")
            self.lastnamesLineEdit.setFocus()
            return False
        elif country == "":
            self.message_box(title="Atención", message="Revise el Formato:\n1. No se ha seleccionado ciudad")
            return False
        else: 
            return True

    
    """
        Validación del empleado
    """
    def validate_employee(self) -> bool:
        
        if self.employeeCheckBox.isChecked():
            salary = (self.salaryLineEdit.text()).strip()
            hire_date = (self.hiringDateEdit.text()).strip()

            if not salary.isnumeric(): 
                self.message_box(title="Atención", message="Revise el Formato:\n1. Solo números para Salario")
                self.salaryLineEdit.setFocus()
                return False
            elif hire_date == "":
                self.message_box(title="Atención", message="Revise el Formato:\n1. Seleccione una fecha de contratación")
                return False
            else: 
                return True
                
                
    """
        Validación del cliente
    """
    def validate_client(self) -> bool:
        
        passport = (self.passportLineEdit.text()).strip()
        if passport == "":
            self.message_box(title="Atención", message="Revise el Formato:\n1. Ingrese su pasaporte")
            self.passportLineEdit.setText("")
            self.passportLineEdit.setFocus()
            return False
        elif not re.match(r"[a-zA-Z0-9]{12}", passport): 
            self.message_box(title="Atención", message="Revise el Formato:\n1. La longitud del pasaporte es erronea (12 carácteres)\n2. Solo alfanúmericos")
            self.passportLineEdit.setFocus()
            return False
        else: 
            return True


    """
        Registro del número de teléfono
    """
    def phone_register(self): 
        
        #Registro de usuario
        if self.tabWidget.currentIndex() == 1: 
            area = (self.areaLineEdit.text()).strip()
            phone = (self.phoneNumberLineEdit.text()).strip()
            
            if area == "" :
                self.message_box(title="Atención", message="Revise el Formato:\n1. Area de teléfono vacío")
                self.areaLineEdit.setFocus()

            elif phone == "":
                self.message_box(title="Atención", message="Revise el Formato:\n1. Número de teléfono vacío")
                self.phoneNumberLineEdit.setFocus()

            elif not re.match(r"\+\d{1,3}", area): 
                self.message_box(title="Atención", message="Revise el Formato:\n1. El número de área debe cumplir: +###, +## o +#\n2. Solo números")
                self.areaLineEdit.setText("")
                self.areaLineEdit.setFocus()
                    
            elif not re.match(r"\d+", phone): 
                self.message_box(title="Atención", message="Revise el Formato:\n1. Solo números para el número de teléfono")
                self.phoneNumberLineEdit.setText()
                self.phoneNumberLineEdit.setFocus()
                    
            else: 

                self.phonenumber[self.count] = [area, phone]
                self.message_box(title="Mensaje", message="Agregado éxitosamente")
                self.count +=1

                self.areaLineEdit.setText("")
                self.phoneNumberLineEdit.setText("")

                print(self.phonenumber)
    

    """
        Eliminar número actual
    """
    def delete_phonenumber(self): 
        
        self.areaLineEdit.setText()
        self.phoneNumberLineEdit.setText()

    
    """
        Obtiene el id del último usuario registrado
    """
    def get_last_id_user(self) -> int: 
        try: 
            get_last_id_user = (self.engine.select(query="SELECT id FROM vw_getLastIdUser")).pop()
            return get_last_id_user[0] + 1
        except IndexError as ie: 
            print("No existen usuarios en la tabla: {}".format(ie))


    """
        Obtiene el id de un país, a partir del nombre del país
    """
    def get_country(self, country: str) -> int: 
        try: 
            query = "SELECT id FROM Country WHERE tex_name = '{}'".format(country)
            print( query )

            transaction = self.engine.select(query=query).pop()
            return transaction[0]

        except IndexError as ie: 
            print("No existe un valor para country: {}".format(ie))
        except sqlite3.OperationalError as soe: 
            print("Error con el nombre de las tablas {}".format(soe))


    """
        Agrega los países al combo box
    """
    def add_country_combo_box(self) -> None: 
        
        try: 
            countries = list(map(lambda x: x[0], self.engine.select(query="SELECT tex_name FROM Country")))
            
            self.countryComboBox.addItems(countries)
        except IndexError as ie: 
            print("Tabla 'Country' vacía {}".format(ie))
        except sqlite3.OperationalError as soe: 
            print("Error con el nombre de las tablas {}".format(soe))




    """
        Limpia los LineEdit, ComboBox y CheckBox
        de la pantalla Registro
    """
    def clean_register_user_screen(self) -> None:

        self.lastnamesLineEdit.setText("")
        self.passportLineEdit.setText("")
        self.employeeCheckBox.setChecked(False)
        self.countryComboBox.setCurrentIndex(0)
        self.salaryLineEdit.setText("")
        self.namesLineEdit.setText("")