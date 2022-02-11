from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from Controllers.mapapi_PG import show_map


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.map_image = QtWidgets.QLabel(self.centralwidget)
        self.map_image.setGeometry(QtCore.QRect(9, 5, 701, 601))
        self.map_image.setText("")
        self.map_image.setObjectName("map_image")
        self.map_image.setPixmap(QPixmap.fromImage(show_map()))

        self.map_Button = QtWidgets.QPushButton(self.centralwidget)
        self.map_Button.setGeometry(QtCore.QRect(740, 10, 113, 32))
        self.map_Button.setObjectName("map_Button")

        self.hybrid_button = QtWidgets.QPushButton(self.centralwidget)
        self.hybrid_button.setGeometry(QtCore.QRect(740, 70, 113, 32))
        self.hybrid_button.setObjectName("hybrid_button")

        self.sat_button = QtWidgets.QPushButton(self.centralwidget)
        self.sat_button.setGeometry(QtCore.QRect(740, 40, 113, 32))
        self.sat_button.setObjectName("sat_button")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(740, 110, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(740, 150, 131, 61))
        self.clear_button.setObjectName("clear_button")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(740, 230, 221, 111))
        self.textEdit.setObjectName("textEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 210, 221, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(740, 350, 211, 41))
        self.label_2.setObjectName("label_2")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(950, 360, 87, 20))
        self.checkBox.setObjectName("checkBox")

        self.find_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_button.setGeometry(QtCore.QRect(890, 150, 131, 61))
        self.find_button.setObjectName("find_button")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.map_Button.setText(_translate("MainWindow", "Карта"))
        self.hybrid_button.setText(_translate("MainWindow", "Гибрид"))
        self.sat_button.setText(_translate("MainWindow", "Спутник"))
        self.clear_button.setText(_translate("MainWindow", "Сброс"))
        self.label.setText(_translate("MainWindow", "Полный адрес объекта"))
        self.label_2.setText(_translate("MainWindow", "Индекс в полном адерсе: да/нет"))
        self.checkBox.setText(_translate("MainWindow", "Да"))
        self.find_button.setText(_translate("MainWindow", "Поиск объекта"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = MapWindow()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())
