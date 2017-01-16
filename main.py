#!/usr/bin/env python

import commands

hmc8043 = "/dev/usbtmc0"

my_hmc = open(hmc8043, "rb+")

my_hmc.write("INST OUT1\n")
my_hmc.write("VOLT 10\n")
my_hmc.write("INST OUT1\n")
my_hmc.write("CURR 3\n")
my_hmc.write("VOLT ?\n")
print my_hmc.read(10)

my_hmc.close()

def main():
    pass

if __name__ == "__main__":
    main()