#importing the modules
# Pyserial 
# Author: Yosia Lukumai

import serial
import time

class ReadFromComPorts:
    comPort = ""

    def __init__(self, comportname: str , baudrate: int , timeout=None):
        """
        Initialize the com port and baudrate then we create the virual port that can be shared
        """
        self.comportname = comportname
        self.baudrate = baudrate
        self.timeout = timeout
    
    @property
    def comPort(self):
        """
        This decorator will setup the comport 
        return : serial object with the port details
        """
        try:
            if(self.timeout == None):
                comPort = serial.Serial(self.comportname, self.baudrate)
                return comPort
            else:
                comPort = serial.Serial(self.comportname, self.baudrate, self.timeout)
                return comPort
        except serial.serialutil.SerialException as err:
            print("---> The port can't be found configure it make sure is  seen by your computer {}".format(self.comportname))
    
    @comPort.setter
    def comPort(self, comportname: str , baudrate:int , timeout: None):
        """
        Set up the comport if there are the changes

        return: serial object with the port info
        """
        comPort = serial.Serial(comportname, baudrate, timeout)
        return comPort
    
    def openPorts(self):
        """
        This will open the ports
        return: None
        """
        try:
            if(self.comPort.is_open):
                print("---> Port already opened")
            else:
                self.comPort.open()
        except (AttributeError, Exception ) as e:
            print("---> Configure well your ports {}".format(self.comportname))

    def checkifTheComportisOpen(self):
        try:
            if(self.comPort.is_open):
                print(self.comPort.is_open)
                print(">>>>> Port is open ready for use")
            else:
                print(">>>> Port is not open")
        except Exception as e:
            print("---> Configure your port {} well ".format(self.comportname))

    
    def closePort(self):
        """
        This will be used for closing the port
        return: 
        """
        try:
            if(self.comPort.is_open == False):
                print("---> Port is not opened")
            else:
                print("here is {}".format(self.comPort.is_open))
                return self.comPort.close()
        except Exception as e:
            print(">>> something has went wrong restart the script")
        
    
    def readCharacters(self):
        """
        This  will return the character from the communication port that has been obtained after reading
        return: 
        Sequence: characters that has been obtained from the comp port
        """





com1 = ReadFromComPorts("COM1", 9600)
com1.checkifTheComportisOpen()
com1.closePort()
com1.checkifTheComportisOpen()