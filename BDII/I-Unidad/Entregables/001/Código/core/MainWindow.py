# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(850, 611)
        MainWindow.setMinimumSize(QtCore.QSize(850, 520))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 851, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(851, 521))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.EntrarSalir = QtWidgets.QWidget()
        self.EntrarSalir.setObjectName("EntrarSalir")
        self.operDoorPushButton = QtWidgets.QPushButton(self.EntrarSalir)
        self.operDoorPushButton.setGeometry(QtCore.QRect(330, 430, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operDoorPushButton.setFont(font)
        self.operDoorPushButton.setObjectName("operDoorPushButton")
        self.label_14 = QtWidgets.QLabel(self.EntrarSalir)
        self.label_14.setGeometry(QtCore.QRect(300, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.layoutWidget = QtWidgets.QWidget(self.EntrarSalir)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 200, 701, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.idLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idLineEdit.setFont(font)
        self.idLineEdit.setStyleSheet("")
        self.idLineEdit.setInputMask("")
        self.idLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.idLineEdit.setObjectName("idLineEdit")
        self.gridLayout_5.addWidget(self.idLineEdit, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.EntrarSalir)
        self.layoutWidget1.setGeometry(QtCore.QRect(370, 290, 73, 76))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.tabWidget.addTab(self.EntrarSalir, "")
        self.Registro = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Registro.setFont(font)
        self.Registro.setObjectName("Registro")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.Registro)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 80, 701, 156))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.passportLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passportLineEdit.setFont(font)
        self.passportLineEdit.setStyleSheet("")
        self.passportLineEdit.setInputMask("")
        self.passportLineEdit.setMaxLength(12)
        self.passportLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passportLineEdit.setObjectName("passportLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.passportLineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.namesLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.namesLineEdit.setFont(font)
        self.namesLineEdit.setStyleSheet("")
        self.namesLineEdit.setInputMask("")
        self.namesLineEdit.setMaxLength(25)
        self.namesLineEdit.setFrame(True)
        self.namesLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.namesLineEdit.setObjectName("namesLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.namesLineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lastnamesLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastnamesLineEdit.setFont(font)
        self.lastnamesLineEdit.setStyleSheet("")
        self.lastnamesLineEdit.setInputMask("")
        self.lastnamesLineEdit.setMaxLength(25)
        self.lastnamesLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lastnamesLineEdit.setObjectName("lastnamesLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastnamesLineEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.countryComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.countryComboBox.setFont(font)
        self.countryComboBox.setCurrentText("")
        self.countryComboBox.setObjectName("countryComboBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.countryComboBox)
        self.label_9 = QtWidgets.QLabel(self.Registro)
        self.label_9.setGeometry(QtCore.QRect(380, 320, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.layoutWidget2 = QtWidgets.QWidget(self.Registro)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 240, 701, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.employeeCheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employeeCheckBox.setFont(font)
        self.employeeCheckBox.setObjectName("employeeCheckBox")
        self.gridLayout_2.addWidget(self.employeeCheckBox, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.salaryLineEdit.setFont(font)
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.gridLayout_2.addWidget(self.salaryLineEdit, 0, 2, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.Registro)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 280, 701, 36))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setToolTip("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.hiringDateEdit = QtWidgets.QDateEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hiringDateEdit.setFont(font)
        self.hiringDateEdit.setObjectName("hiringDateEdit")
        self.gridLayout_3.addWidget(self.hiringDateEdit, 0, 1, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.Registro)
        self.layoutWidget4.setGeometry(QtCore.QRect(70, 350, 701, 36))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.areaComboBox = QtWidgets.QComboBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.areaComboBox.setFont(font)
        self.areaComboBox.setObjectName("areaComboBox")
        self.gridLayout.addWidget(self.areaComboBox, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.phoneNumberLineEdit.setFont(font)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")
        self.gridLayout.addWidget(self.phoneNumberLineEdit, 0, 3, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.Registro)
        self.layoutWidget5.setGeometry(QtCore.QRect(250, 430, 297, 88))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.addPushButton = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addPushButton.setFont(font)
        self.addPushButton.setObjectName("addPushButton")
        self.gridLayout_4.addWidget(self.addPushButton, 0, 0, 1, 1)
        self.deletePushButton = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deletePushButton.setFont(font)
        self.deletePushButton.setObjectName("deletePushButton")
        self.gridLayout_4.addWidget(self.deletePushButton, 0, 1, 1, 1)
        self.registerPushButton = QtWidgets.QPushButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.registerPushButton.setFont(font)
        self.registerPushButton.setObjectName("registerPushButton")
        self.gridLayout_4.addWidget(self.registerPushButton, 1, 0, 1, 2)
        self.tabWidget.addTab(self.Registro, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(240, 210, 361, 121))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setHorizontalSpacing(50)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.userLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLineEdit.setFont(font)
        self.userLineEdit.setStyleSheet("")
        self.userLineEdit.setInputMask("")
        self.userLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.userLineEdit.setObjectName("userLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userLineEdit)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("")
        self.passwordLineEdit.setInputMask("")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.LoginPushButton = QtWidgets.QPushButton(self.tab)
        self.LoginPushButton.setGeometry(QtCore.QRect(340, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LoginPushButton.setFont(font)
        self.LoginPushButton.setObjectName("LoginPushButton")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(320, 140, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_2)
        self.treeWidget.setGeometry(QtCore.QRect(90, 160, 671, 271))
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(155)
        self.treeWidget.header().setHighlightSections(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(230, 45, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Air Canadá Center"))
        self.operDoorPushButton.setText(_translate("MainWindow", "Abrir Puerta"))
        self.label_14.setText(_translate("MainWindow", "Ingrese su ID"))
        self.label_2.setText(_translate("MainWindow", "Id"))
        self.idLineEdit.setToolTip(_translate("MainWindow", "Ingrese el ID proporcionado por el administrador"))
        self.radioButton.setText(_translate("MainWindow", "Entrar"))
        self.radioButton_2.setText(_translate("MainWindow", "Salir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EntrarSalir), _translate("MainWindow", "Entrar/Salir"))
        self.label_3.setText(_translate("MainWindow", "Número de Pasaporte"))
        self.passportLineEdit.setToolTip(_translate("MainWindow", "Ingrese un número de Pasaporte"))
        self.label_4.setText(_translate("MainWindow", "Nombres"))
        self.namesLineEdit.setToolTip(_translate("MainWindow", "Ingrese sus nombres"))
        self.label_5.setText(_translate("MainWindow", "Apellidos"))
        self.lastnamesLineEdit.setToolTip(_translate("MainWindow", "Ingrese sus apellidos"))
        self.label_6.setText(_translate("MainWindow", "País de Procedencia"))
        self.countryComboBox.setToolTip(_translate("MainWindow", "Seleccione el país"))
        self.label_9.setText(_translate("MainWindow", "Teléfonos"))
        self.employeeCheckBox.setToolTip(_translate("MainWindow", "Marque si es un Empleado"))
        self.employeeCheckBox.setText(_translate("MainWindow", "Empleado"))
        self.label_12.setText(_translate("MainWindow", "Salario"))
        self.salaryLineEdit.setToolTip(_translate("MainWindow", "Inserte el salario del empleado"))
        self.label_13.setText(_translate("MainWindow", "Fecha de Contratación"))
        self.hiringDateEdit.setToolTip(_translate("MainWindow", "Seleccione la fecha de contratación"))
        self.label_10.setText(_translate("MainWindow", "Área"))
        self.areaComboBox.setToolTip(_translate("MainWindow", "Seleccione el código de área"))
        self.label_11.setText(_translate("MainWindow", "Teléfono"))
        self.phoneNumberLineEdit.setToolTip(_translate("MainWindow", "Introduzca el número de teléfono"))
        self.addPushButton.setToolTip(_translate("MainWindow", "Agregue un campo nuevo de teléfono"))
        self.addPushButton.setText(_translate("MainWindow", "Agregar Teléfono"))
        self.deletePushButton.setToolTip(_translate("MainWindow", "Elimine el campo de teléfono actual"))
        self.deletePushButton.setText(_translate("MainWindow", "Eliminar Teléfono"))
        self.registerPushButton.setToolTip(_translate("MainWindow", "Registrar"))
        self.registerPushButton.setText(_translate("MainWindow", "Registrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Registro), _translate("MainWindow", "Registro"))
        self.label_7.setText(_translate("MainWindow", "Usuario"))
        self.userLineEdit.setToolTip(_translate("MainWindow", "Ingrese un número de Pasaporte"))
        self.passwordLineEdit.setToolTip(_translate("MainWindow", "Ingrese un número de Pasaporte"))
        self.label_8.setText(_translate("MainWindow", "Contraseña"))
        self.LoginPushButton.setToolTip(_translate("MainWindow", "Inicie sesión"))
        self.LoginPushButton.setText(_translate("MainWindow", "Iinicar Sesión"))
        self.label_15.setText(_translate("MainWindow", "Ingrese datos de acceso"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Administrador"))
        #self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Id"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Nombre"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Actividad"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Usuario"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Fecha"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Histórico"))
        self.label_16.setText(_translate("MainWindow", "Air Canadá Center"))
