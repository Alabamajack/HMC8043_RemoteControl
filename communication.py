#!/usr/bin/env python

class Communication:
    def __init__(self):
        self._device = ""
        self.__connection = None
        self.__isOpen = False
    
    def Open(self):
        self.__connection = open(self._device, 'rb+')
        self.__isOpen = True
    
    def Read(self, length):
        if not self.__isOpen:
            self.Open()
        return self.__connection.read(length)
    
    def Write(self, message):
        if not self.__isOpen:
            self.Open()
        self.__connection.write(message)
    
    def Close(self):
        self.__connection.close()
        self.__isOpen = False


class CommUSBTMC(Communication):
    def __init__(self, device_path):
        Communication.__init__(self)
        self._device = device_path
        
        
if __name__ == "__main__":
    mycomm = CommUSBTMC("/dev/usbtmc0")
    mycomm.Open()
    mycomm.Write("INST:NSEL 1\n")
    mycomm.Write("VOLT?\n")
    print mycomm.Read(10)
    mycomm.Close()