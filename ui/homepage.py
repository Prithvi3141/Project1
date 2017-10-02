# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(170, 70, 161, 21))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(170, 110, 161, 21))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 150, 161, 21))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.mainLabel = QtWidgets.QLabel(Form)
        self.mainLabel.setGeometry(QtCore.QRect(110, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.temperatureLabel = QtWidgets.QLabel(Form)
        self.temperatureLabel.setGeometry(QtCore.QRect(50, 70, 91, 21))
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.humidityLabel = QtWidgets.QLabel(Form)
        self.humidityLabel.setGeometry(QtCore.QRect(50, 110, 81, 21))
        self.humidityLabel.setObjectName("humidityLabel")
        self.timeLabel = QtWidgets.QLabel(Form)
        self.timeLabel.setGeometry(QtCore.QRect(50, 150, 111, 21))
        self.timeLabel.setObjectName("timeLabel")
        self.refreshPushButton = QtWidgets.QPushButton(Form)
        self.refreshPushButton.setGeometry(QtCore.QRect(20, 200, 101, 31))
        self.refreshPushButton.setObjectName("refreshPushButton")
        self.averageButton = QtWidgets.QPushButton(Form)
        self.averageButton.setGeometry(QtCore.QRect(140, 200, 101, 31))
        self.averageButton.setObjectName("averageButton")
        self.quitButton = QtWidgets.QPushButton(Form)
        self.quitButton.setGeometry(QtCore.QRect(260, 200, 101, 31))
        self.quitButton.setObjectName("quitButton")
        self.alertLabel = QtWidgets.QLabel(Form)
        self.alertLabel.setGeometry(QtCore.QRect(20, 30, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(143, 146, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.alertLabel.setPalette(palette)
        self.alertLabel.setObjectName("alertLabel")

        self.retranslateUi(Form)
#        self.quitButton.clicked.connect(Form.close)
#        self.refreshPushButton.clicked.connect(Form.refreshRead)
#        self.averageButton.clicked.connect(Form.average)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mainLabel.setText(_translate("Form", "Thermostat"))
        self.temperatureLabel.setText(_translate("Form", "Temperature"))
        self.humidityLabel.setText(_translate("Form", "Humidity"))
        self.timeLabel.setText(_translate("Form", "Recording Time"))
        self.refreshPushButton.setText(_translate("Form", "Refresh"))
        self.averageButton.setText(_translate("Form", "Average"))
        self.quitButton.setText(_translate("Form", "Quit"))
        self.alertLabel.setText(_translate("Form", "*Error reading data from sensor \n"
" Hit refresh again"))

