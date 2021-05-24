# -*- coding: utf-8 -*-

from core.MainWindow import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow

class App(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.registerPushButton.clicked.connect(self.prueba)
    
    # Aquí van los métodos para controlar la interfáz
    def prueba(self):
        print("Registro")


    