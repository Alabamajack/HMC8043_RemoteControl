#!/usr/bin/env python

class Communication:
    def __init__(self, device_path):
        self._device = device_path
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
        
        
if __name__ == "__main__":
    pass