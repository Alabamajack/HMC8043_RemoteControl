#!/usr/bin/env python

import argparse
import commands
import re

VERSION = 0.1

def mystrin(v):
    if not re.search("(SetVoltage|GetVoltage):(1|2|3)(:\d|)", v):
        raise argparse.ArgumentTypeError("Error")
    else:
        return v

def main():
    parser = argparse.ArgumentParser(description="Command line interface to send commands to power supplies")
    parser.add_argument('-d', '--device', default='HMC8043', choices=['HMC8043'], help='specifies which device should be remote controlled')
    parser.add_argument('-c', '--connection', choices=['USBTMC'], default='USBTMC', help='specifies the connection type to the remote device')
    parser.add_argument('-V', '--version', help='returns the version', action='version', version='Power Supply Remote Control V' + str(VERSION))
    
    #parser.add_argument('Command', nargs = 1, type=mystrin, action='append', choices=[x for x in dir(commands.Commands) if not re.search("^(__|_).*", x)], help='specifies the commando which should be sended to the remote device')
    #parser.add_argument('Channel', nargs = 1, type=str, choices=['1','2','3'], help='specifies the channel which you want to select')
    #parser.add_argument('Value', nargs='?', help='the value for the command. optional for some commands like GetVoltage')
    parser.add_argument('-C', type=mystrin, action='append')
    
    args = parser.parse_args()
    print args
    
if __name__ == "__main__":
    main()