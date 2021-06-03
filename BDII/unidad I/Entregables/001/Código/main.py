# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from core.App import App
from core.SQLiteEngine import SQLiteEngine

if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    application = App()
    application.show()

    sys.exit(app.exec_())