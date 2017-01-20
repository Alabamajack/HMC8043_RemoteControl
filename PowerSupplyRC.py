#!/usr/bin/env python

import argparse
import commands
import re
import cmd
from commands import HMC804xDevice

VERSION = 0.1

def ValidCommands(v):
    choices=[x for x in dir(commands.Device) if not re.search("^(__|_).*", x)]
    if not re.search("(?:" + '|'.join(choices) + ")\:\d(?:\:\d+\.\d+|\:\d+|)$", v):
        raise argparse.ArgumentTypeError("Error")
    else:
        return v
    
class InterActiveConsole(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        #setattr(InterActiveConsole, name, value)
    
    def do_greet(self, line):
        print "hello"
    def do_EOF(self, line):
        return True

def main():
    parser = argparse.ArgumentParser(description="Command line interface to send commands to power supplies")
    parser.add_argument('-d', '--device', default='HMC8043', choices=['HMC8043'], help='specifies which device should be remote controlled')
    parser.add_argument('-c', '--connection', default='/dev/usbtmc0', help='specifies the connection type to the remote device')
    parser.add_argument('-V', '--version', help='returns the version', action='version', version='Power Supply Remote Control V' + str(VERSION))
    parser.add_argument('-C', '--Command', type=ValidCommands, action='append', help='the command you want to send')
    parser.add_argument('-i', '--interactive', action='store_true', help='entering the interactive mode where commands can send to the device. With this flag, all -C arguments will be ignored!')
    
    args = vars(parser.parse_args())
#    print args
    #now must parsing the functions and call them
    
    conn = args['connection']
    dev = args['device']
    
    if dev == 'HMC8043':
        comm = HMC804xDevice(conn)
    else:
        comm = None
    
    print args
    
    if args['interactive']:
        InterActiveConsole().cmdloop()
    else:
        if args['Command'] != None:
            for arg in args['Command']:
                param = arg.split(':')
                method = getattr(comm, param[0])
                method(int(param[1]), float(param[2]))
    
if __name__ == "__main__":
    main()