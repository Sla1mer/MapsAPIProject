from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QKeyEvent
from io import BytesIO
from PIL import ImageQt, Image
from Controllers.get_map_img import get_map_image
from PyQt5.QtCore import Qt
import sys
from Controllers.get_coord_by_name import get_coord
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from Controllers.mapapi_PG import show_map
from Models.Variables import coord, spn
globality_mode = 'map'
all_pt = []
pt_query = ''

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 600
        self.btn = None

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1027, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.map_image = QtWidgets.QLabel(self.centralwidget)
        self.map_image.setGeometry(QtCore.QRect(9, 5, 701, 601))
        self.map_image.setText("")
        self.map_image.setObjectName("map_image")
        self.map_image.setPixmap(QPixmap.fromImage(show_map()))

        self.map_Button = QtWidgets.QPushButton(self.centralwidget)
        self.map_Button.setGeometry(QtCore.QRect(740, 10, 113, 32))
        self.map_Button.setObjectName("map_Button")
        self.map_Button.clicked.connect(lambda: self.change_mode('map'))

        self.hybrid_button = QtWidgets.QPushButton(self.centralwidget)
        self.hybrid_button.setGeometry(QtCore.QRect(740, 70, 113, 32))
        self.hybrid_button.setObjectName("hybrid_button")
        self.hybrid_button.clicked.connect(lambda: self.change_mode('sat,skl'))

        self.sat_button = QtWidgets.QPushButton(self.centralwidget)
        self.sat_button.setGeometry(QtCore.QRect(740, 40, 113, 32))
        self.sat_button.setObjectName("sat_button")
        self.sat_button.clicked.connect(lambda: self.change_mode('sat'))

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(740, 110, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(740, 150, 131, 61))
        self.clear_button.setObjectName("clear_button")
        self.clear_button.clicked.connect(lambda: self.del_last_pt())

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
        self.find_button.clicked.connect(lambda: self.find_obj(self.lineEdit.text()))

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def find_obj(self, name):
        global coord, all_pt
        try:
            coord = get_coord(name)
            if coord not in all_pt:
                all_pt.append(coord)
            self.add_pt()
            self.update_map()
        except KeyError:
            pass

    def add_pt(self):
        global pt_query, all_pt
        temp = []
        for i in all_pt:
            temp.append(f'{i[0]},{i[1]}')
        pt_query = '~'.join(temp)

    def del_last_pt(self):
        global all_pt
        self.lineEdit.clear()
        try:
            del all_pt[-1]
            print(all_pt)
            print(pt_query)
            self.add_pt()
            self.update_map()
        except IndexError:
            pass

    def change_mode(self, mode):
        global globality_mode
        globality_mode = mode
        self.update_map()

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

    def mousePressEvent(self, event):
        if self.lineEdit.hasFocus():
            self.lineEdit.clearFocus()

        if self.textEdit.hasFocus():
            self.textEdit.clearFocus()

    def update_map(self):
        print(pt_query)
        self.map_image.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(Image.open(BytesIO(
            get_map_image(f'l={globality_mode}', f'll={coord[0]},{coord[1]}', f'spn={spn[0]},{spn[0]}', f'pt={pt_query}'))))))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            coord[0] = str(float(coord[0]) - 0.001)
            self.update_map()

        if event.key() == Qt.Key_Right:
            coord[0] = str(float(coord[0]) + 0.001)
            self.update_map()

        if event.key() == Qt.Key_Up:
            coord[1] = str(float(coord[1]) + 0.001)
            self.update_map()

        if event.key() == Qt.Key_Down:
            coord[1] = str(float(coord[1]) - 0.001)
            self.update_map()

        if event.key() == Qt.Key_PageUp:
            if 0 < spn[0] - 0.001 < 0.1:
                spn[0] -= 0.002
            self.update_map()

        if event.key() == Qt.Key_PageDown:
            if spn[0] + 0.003 < 0.05100000000000001:
                spn[0] += 0.003
            self.update_map()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = MapWindow()
    ui.setupUi()

    ui.show()
    sys.exit(app.exec_())
