# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'average.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Average(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(widget)
        self.textBrowser.setGeometry(QtCore.QRect(170, 80, 161, 21))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(170, 120, 161, 21))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(widget)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 160, 161, 21))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.mainLabel = QtWidgets.QLabel(widget)
        self.mainLabel.setGeometry(QtCore.QRect(100, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")
        self.temperatureLabel = QtWidgets.QLabel(widget)
        self.temperatureLabel.setGeometry(QtCore.QRect(30, 80, 141, 21))
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.humidityLabel = QtWidgets.QLabel(widget)
        self.humidityLabel.setGeometry(QtCore.QRect(30, 120, 111, 21))
        self.humidityLabel.setObjectName("humidityLabel")
        self.timeLabel = QtWidgets.QLabel(widget)
        self.timeLabel.setGeometry(QtCore.QRect(30, 160, 121, 21))
        self.timeLabel.setObjectName("timeLabel")
        self.refreshPushButton = QtWidgets.QPushButton(widget)
        self.refreshPushButton.setGeometry(QtCore.QRect(50, 210, 101, 31))
        self.refreshPushButton.setObjectName("refreshPushButton")
        self.quitButton = QtWidgets.QPushButton(widget)
        self.quitButton.setGeometry(QtCore.QRect(210, 210, 101, 31))
        self.quitButton.setObjectName("quitButton")

        self.retranslateUi(widget)
        #self.quitButton.clicked.connect(widget.close)
        #self.refreshPushButton.clicked.connect(widget.refreshRead)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.mainLabel.setText(_translate("widget", "Average Readings"))
        self.temperatureLabel.setText(_translate("widget", "Mean Temperature"))
        self.humidityLabel.setText(_translate("widget", "Mean Humidity"))
        self.timeLabel.setText(_translate("widget", "Calculation Time"))
        self.refreshPushButton.setText(_translate("widget", "Recalculate"))
        self.quitButton.setText(_translate("widget", "Quit"))

