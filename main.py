from usbtmc import usbtmc

instr =  usbtmc.Instrument("USB::0x0AAD::0x0135::INSTR")
print instr.ask("*IDN?")