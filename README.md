Project 1 EID-Fall2017

Repo for Project 1 Fall 2017 Embedded Interface Design class Prithvi Teja Veeravalli

To run Project 1 on your Raspberry Pi follow the following steps:-

Install or upgrade your python version to python 3.5

Install PyQt5 using the following command

      sudo apt-get install python3-pyqt5
      
Clone the Adafruit_DHT_Python library from github

      git clone https://github.com/adafruit/Adafruit_Python_DHT.git
      
->Install the library executable i.e.

      sudo python setup.py install
      
Project 1 has the following features:

-> Project 1 aims at developing a rudimentary thermostat making use of Raspberry Pi, DHT22 Temperature/Humidity sensor and QT for gui 
   or interface development.
   
-> As part of the requirements UI allows for request of temperature and humidity values and displays the time of recording of temperature and humidity.
   
-> The UI handles not receiving data gracefully. UI shows an error stating that data has not been received and it informs the user to make a request again.

  
 Extra-Credit Work
 
 -> Retrieves Temperature and Humidity values periodically and stores them to calculate mean temperature and mean humidity
 
 -> If the temperature is outside of the permissible limits of temperature an alarm or alert for high or low value is delivered in the 

form of a Warning Message Box. Permissible limits of temperature are [10, 40]

-> If the humidity is outside of the permissible limits of humidity an alarm or alert for high or low value is delivered in the form of

a Warning Message Box. Permissible limits of humidity are [30, 90]
