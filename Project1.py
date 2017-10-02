#!/usr/bin/env python
""" This Project1.py script is build to act as a simple thermostat and humidity sensor. The functionality present in
this simple thermostat is that it allows for the request of temperature and pressure, it retrieves temp/humidity
values periodically and stores it to calculate the mean over time. This simple thermostat also has an alarm i.e. a
Warning Box pops up if the temperature or humidity is outside the permissible limits"""


import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout, QMessageBox
from PyQt5 import QtCore
from ui.homepage import Ui_Form
from ui.average import Ui_Average


from datetime import datetime
import time

import Adafruit_DHT
import threading
import numpy as np

__author__ = "Prithvi Teja Veeravalli"
__copyright__ = "Copyright (C) 2017 by Prithvi Teja Veeravalli"
#
# Redistribution, modification or use of this software in source or binary
# forms is permitted as long as the files maintain this copyright. Users are
# permitted to modify this and use it to learn about the field of embedded
# software. Prithvi Teja Veeravalli, and the University of Colorado
# are not liable for any misuse of this material.
#


listTemperature = []      #list used to store temperature readings
listHumidity = []         #list used to store humidity readings
listDateTime = []         #list used to store date and time of temperature and humidity recordings
i = [0]
sensor = 22               #Initializing sensor to be DHT22 for telling the Adafruit_DHT Library.
pin = 4                   #Data line of DHT22 is connected to GPIO4

#This class is used to display the ui page for average
class Average(Ui_Average, QWidget):

        #This function is used to init the Average tab
        def __init__(self, callerObject):
                QWidget.__init__(self)
                self.setupUi(self)
                self.refreshPushButton.clicked.connect(self.refreshRead)
                self.quitButton.clicked.connect(callerObject.closeAvgTab)


        #This function is used to refresh or update the average temperature and humidity 
        def refreshRead(self):
                li = np.vstack((listDateTime, listTemperature, listHumidity))
                #li = sorted(li,key= lambda li: li[0])
                tempAvg = np.mean(listTemperature)
                humidAvg = np.mean(listHumidity)
                dateTime = datetime.today()
                print ("listTemperature: ", listTemperature[0:10], "\n")       
                print ('Average Temperature: {0:0.1f}'.format(tempAvg))

                temper = '{0:0.2f}'.format(tempAvg) + ' C'
                humid = '{0:0.2f}'.format(humidAvg) + ' %'
                date = '{:%Y-%m-%d %H:%M}'.format(dateTime)

                
                self.textBrowser.setText(temper)
                self.textBrowser_2.setText(humid)
                self.textBrowser_3.setText(date)

#This class is used to display the homepage of the thermostat
class Form(Ui_Form, QWidget):
        #This function is used to init the homepage tab
        def __init__(self, callerObject):
                QWidget.__init__(self)
                self.setupUi(self)
                self.refreshPushButton.clicked.connect(self.refreshRead)
                self.averageButton.clicked.connect(callerObject.aver)                
                self.quitButton.clicked.connect(callerObject.closeApp)
                
        #This function is used to requestcurrent temperature and humidity values
        def refreshRead(self):
                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin, retries = 2, delay_seconds = 0 )
                dateTime = datetime.today()
                
        # Un-comment the line below to convert the temperature to Fahrenheit.
        # temperature = temperature * 9/5.0 + 32
                if humidity is not None and temperature is not None:
                        temper = '{0:0.1f}'.format(temperature) + ' C'
                        humid = '{0:0.1f}'.format(humidity) + ' %'
                        date = '{:%Y-%m-%d %H:%M}'.format(dateTime)

                        #The following 3 lines are used to display the recorded temp & humidity values in the text browser 
                        self.textBrowser.setText(temper)
                        self.textBrowser_2.setText(humid)
                        self.textBrowser_3.setText(date)
                        
                        _translate = QtCore.QCoreApplication.translate
                        self.alertLabel.setText(_translate("Form", ""))
                        self.show()
                        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
                        print('{:%Y-%m-%d %H:%M}'.format(dateTime))
                else:
                        #This snippet is used for error handling i.e. if the sensor doesn't return the values
                        _translate = QtCore.QCoreApplication.translate
                        self.alertLabel.setText(_translate("Form", "*Error receiving data from the sensor. \n Hit refresh again"))
                        self.show()
                
#This class is used to setup the main window and set the size of the main window
class App(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)
                self.setGeometry(200, 200, 700, 500)
                self.resize(400,350)

                self.windowWidget = OuterWidget(self)
                self.setCentralWidget(self.windowWidget)

                self.setWindowTitle('Thermostat')
                
                self.show()

#This class setsup and outer widget which contains multiple tabs i.e. multiple widgets which are tabs in it.
class OuterWidget(QWidget):

        def __init__(self, callerObject):
                super(QWidget, self).__init__(callerObject)

                self.caller = callerObject

                self.layout = QVBoxLayout(self)
                
                self.tabs = QTabWidget()
                self.tab1 = Form(self)

                self.tabs.setTabsClosable(True)
                self.tabs.tabCloseRequested.connect(self.tabs.removeTab)
                
                self.tab1.refreshRead()

                self.tabs.addTab(self.tab1, "Home")

                self.layout.addWidget(self.tabs)
                self.setLayout(self.layout)
        #This function is to load a tab for Average of Temperature and Humidity
        def aver(self):
                tempAvg = np.mean(listTemperature)
                humidAvg = np.mean(listHumidity)
                dateTime = datetime.today()
                print ("listTemperature: ", listTemperature[0:100], "\n")       
                print ('Average Temperature: {0:0.1f}'.format(tempAvg))

                self.tab2 = Average(self)

                temper = '{0:0.2f}'.format(tempAvg) + ' C'
                humid = '{0:0.2f}'.format(humidAvg) + ' %'
                date = '{:%Y-%m-%d %H:%M}'.format(dateTime)

                
                self.tab2.textBrowser.setText(temper)
                self.tab2.textBrowser_2.setText(humid)
                self.tab2.textBrowser_3.setText(date)

                if self.tabs.count() < 2:
                        averageIndex = self.tabs.addTab(self.tab2, "Mean Values")
                        self.tabs.setCurrentIndex(averageIndex)
                else:
                        self.tabs.setCurrentIndex(1)

        #This function is used to close this rudimentary thermostat application
        def closeApp(self):
                self.tabs.removeTab(1)
                self.tabs.removeTab(0)

                self.layout.removeWidget(self.tabs)
                self.caller.close()

        #This function is used to close the tab that was opened for Mean Data of temperature and Humidity
        def closeAvgTab(self):
                index = self.tabs.currentIndex()
                self.tabs.removeTab(index)

#This function in a dedicated thread for itself periodically retrieve the temperature/humidity values and stores this in a list of 100
#for future use such as calculating mean temperature and humidity values
def threadFunction(app):
        
        while 1:
                sensorReadTable(sensor, pin, app)
                time.sleep(2)

        
#This function is used to read temperature and  humidity values and store them in a list for future historical display
def sensorReadTable(sensor, pin, app):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin, retries = 2, delay_seconds = 0)
        dateTime = datetime.today()

        
        if humidity is not None and temperature is not None:
                if len(listTemperature) <= i[0]:
                        listTemperature.append(temperature)
                        listHumidity.append(humidity)
                        listDateTime.append(dateTime)
                else:
                        del listTemperature[i[0]]
                        del listHumidity[i[0]]
                        del listDateTime[i[0]]
                        listTemperature.insert(i[0], temperature)
                        listHumidity.insert(i[0], humidity)
                        listDateTime.insert(i[0], dateTime)
                print('humidity: ', humidity)

                if(temperature > 40) and (humidity > 70):
                        choice = QMessageBox.warning(app, 'High Temperature & Humidity Alert!', 'Temperature is higher than the threshold of 40. \n Humidity is higher than threshold of 70 %', QMessageBox.Close)
                elif (temperature > 40) and (humidity < 30):
                        choice = QMessageBox.warning(app, 'High Temperature & Low Humidity Alert!', 'Temperature is higher than the threshold of 40 C. \n Humidity is lower than threshold of 30 %', QMessageBox.Close)                                              
                elif temperature > 40:
                        choice = QMessageBox.warning(app, 'High Temperature Alert!', 'Temperature is higher than the threshold of 40 C.', QMessageBox.Close)                                              
                elif (temperature < 10) and (humidity > 70):
                        choice = QMessageBox.warning(app, 'Low Temperature & High Humidity Alert!', 'Temperature is lower than the threshold of 10 C. \n Humidity is higher than threshold of 70 %', QMessageBox.Close)                                              
                elif (temperature < 10) and (humidity < 30):
                        choice = QMessageBox.warning(app, 'Low Temperature & Low Humidity Alert!', 'Temperature is lower than the threshold of 10 C. \n Humidity is lower than threshold of 30 %', QMessageBox.Close)                                              
                elif temperature < 10:
                        choice = QMessageBox.warning(app, 'Low Temperature Alert!', 'Temperature is lower than the threshold of 10 C.', QMessageBox.Close)                                              
                elif humidity < 30:
                        choice = QMessageBox.warning(app, 'Low Humidity Alert!', 'Humidity is lower than the threshold of 30 %.', QMessageBox.Close)                                              
                elif humidity > 70:
                        choice = QMessageBox.warning(app, 'High Humidity Alert!', 'Humidity is higher than the threshold of 70 %.', QMessageBox.Close)                                              
        
        


                if i[0] < 99:
                        i[0] = i[0] + 1
                else:
                        i[0] = 0

def main():
        app = QApplication(sys.argv)

        ex = App() 
        th = threading.Thread(target = threadFunction, args = (ex, ))
        th.start()
        sys.exit(app.exec_())


        
 
if __name__ == "__main__":
        main() 
