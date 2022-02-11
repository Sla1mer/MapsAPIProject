from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map_image = QtWidgets.QLabel(self.centralwidget)
        self.map_image.setGeometry(QtCore.QRect(9, 5, 791, 601))
        self.map_image.setText("")
        self.map_image.setObjectName("map_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = MapWindow()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
