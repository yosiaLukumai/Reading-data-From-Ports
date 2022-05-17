#importing the modules
# Pyserial 
# Author: Yosia Lukumai


import serial
import time

class ReadFromComPorts:
    comPort = ""
    data = []

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
            print(e)

    def checkifTheComportisOpen(self):
        try:
            if(self.comPort.is_open):
                print(self.comPort.is_open)
                print(">>>>> Port is open ready for use")
            else:
                print(">>>> Port is not open")
        except Exception as e:
            print("---> Configure your port {} well ".format(self.comportname))
            print(e)

    
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
            print(e)
        
    
    def readCharacterData(self):
        """
        This  will return the character from the communication port that has been obtained after reading
        return: 
        Sequence: characters that has been obtained from the comp port
        """
        try:
            if(self.comPort.is_open):
                data = self.comPort.read().decode("utf-8")
                return data
        except Exception as e:
            print("---> something has went wrong while trying to read the line from the communication port")
            print(e)
    
    def readLineData(self, splitparameter=' '):
        """
        This methods return the characters received 
        return:
        list - That various data can be separated
        """
        try:
            if self.comPort.is_open:
                print("Reading the line from the comport")
                data = self.comPort.readline()
                dataDecoded = str(data[0: len(data)].decode('utf-8'))
                sortedData = dataDecoded.split(splitparameter)
                sortedData.pop()
                return sortedData
        except Exception as e:
            print("---> something has went wrong while trying to read the line from the communication port")
            print(e)

    
    def sendDataToServer(self):
        pass



com1 = ReadFromComPorts("COM1", 9600)

data = com1.readLineData("xx")
print(data)