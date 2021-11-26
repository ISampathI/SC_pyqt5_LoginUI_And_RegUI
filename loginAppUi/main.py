######################################################
##  SihinaCode > Search YouTube for more tutorials  ##
######################################################

from PyQt5 import QtWidgets, QtCore
from loginUi import Ui_Form
import sys

class LoginApp(QtWidgets.QWidget, Ui_Form):
    def changeForm(self):
        if self.pushButton_7.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.pushButton_7.setText("<")
        else:
            self.widget_2.show()
            self.widget_3.hide()
            self.pushButton_7.setText(">")

    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.widget_3.hide()
        self.pushButton_7.clicked.connect(self.changeForm)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec_())
