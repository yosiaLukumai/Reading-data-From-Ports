#importing the modules
# Pyserial || request || schedule

import serial
import time

class ReadFromComPorts:
    comPort = ""

    def __init__(self, comport: str , baudrate: int , timeout=None):
        """
        Initialize the com port and baudrate then we create the virual port that can be shared
        """
        self.comportname = comport
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
            print("---> The port can't be found configure it :{}".format(self.comportname))
    
    @comPort.setter
    def comPort(self, comportname: str , baudrate:int , timeout: None):
        """
        Set up the comport if there are the changes

        return: serial object with the port info
        """
        print("setting the port")
        comPort = serial.Serial(comportname, baudrate, timeout)
        return comPort
    
    def openPorts(self):
        """
        This will open the ports
        return: None
        """
        print(self.comPort.baudrate)

    
    def closePort(self):
        print(self.comPort.baudrate)





com1 = ReadFromComPorts("COM1", 9600)
com1.comPort