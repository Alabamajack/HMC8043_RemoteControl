#!/usr/bin/env python

from sympy.physics.units import voltage
import communication
from enum import Enum

class GeneralCommand(Enum):
    GetDeviceInformation = 1
    SetVoltage = 2
    GetVoltage = 3
    SetCurrent = 4
    GetCurrent = 5
    SelectChannel = 6
    
class Command():
    def __init__(self, command, length):
        self.command = command
        self.length = length
        
    def __mod__(self, value):
        return self.command % value
    
    def __str__(self):
        return self.command

class Commands:    
    def __init__(self):
        self._GeneralCommands = {
                                  GeneralCommand.GetDeviceInformation : None,
                                  GeneralCommand.SetVoltage : None,
                                  GeneralCommand.GetVoltage : None,
                                  GeneralCommand.SetCurrent : None,
                                  GeneralCommand.GetCurrent : None,
                                  GeneralCommand.SelectChannel : None
                                }
        
    def __SelectChannel(self,channel):    
        self._GeneralCommands[GeneralCommand.SelectChannel] % channel
    
    def SetVoltage(self, channel, voltage):
        self.__SelectChannel(channel)
        self._GeneralCommands[GeneralCommand.SetVoltage] % voltage
        
    def GetVoltage(self, channel):
        self.__SelectChannel(channel)
        self._GeneralCommands[GeneralCommand.GetVoltage]
        
class HMC804xCommands(Commands):
    def __init__(self):
        Commands.__init__(self)
        
        self.__linefeed = "\n"
        self._GeneralCommands[GeneralCommand.SelectChannel] = Command("INST:NSEL %i" + self.__linefeed, None)
        self._GeneralCommands[GeneralCommand.SetVoltage] = Command("VOLT %i" + self.__linefeed, None)
        self._GeneralCommands[GeneralCommand.GetVoltage] = Command("VOLT?" + self.__linefeed, 10)
        
    
class DummyCommands(Commands):
    def __init__(self):
        Commands.__init__(self)
        
        
if __name__ == "__main__":
#     mycommand = HMC804xCommands()
#     mycommand.GetVoltage()
    print dir(Commands)
    