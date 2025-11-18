# Adapted from https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/test_my_design.py

import pytest

import os
from termcolor import colored

import numpy as np

def alu(x,y, code):
    if code == "101010":
        return 0
    elif  code == "111111":
        return 1
    elif code == "111010":
        return 65535 #-1
    elif code == "001100":
        return x
    elif code == "110000":
        return y
    elif code == "001101":
        return ~x
    elif code == "110001":
        return ~y
    elif code == "001111":
        return (65536-x) if (x!= 0) else 0  #-x
    elif code == "110011":
        return (65536-y) if (y!= 0) else 0  #-y
    elif code == "011111":
        return (x+1) if (x < 65535) else 0  #x+1
    elif code == "110111":
        return (y+1) if (y < 65535) else 0  #y+1
    elif code == "001110":
        return (x-1) if (x > 0) else 65535  #x-1
    elif code == "110010":
        return (y-1) if (y > 0) else 65535  #y-1
    elif code == "000010":
        return (x+y) if ( (np.uint32(x)+np.uint32(y)) <= 65535) else (np.uint32(x)+np.uint32(y)-65536)  #x+y
    elif code == "010011":
        return (x-y) if (x >= y) else (65536-(y-x))  #x-y
    elif code == "000111":
        return (y-x) if ( y >= x) else (65536-(x-y))  #y-x
    elif code == "000000":
        return x&y
    elif code == "010101":
        return x|y
    else:
        return 0


def test_CPU():

    erro = 0

    file_test = open("config_testes_nasm.txt","r")
    lines_test = file_test.readlines() 
    file_test.close()

    print("\n\n===================================================")
    for line in lines_test:
        if len(line.strip()):
            if ((line.strip()[0] != '#') and ( line.strip().find('.nasm') > 0 )):
                # pega parametros e atribui caminhos globais
                # par[0] : Nome do teste (subpasta)
                # par[1] : quantidade de testes a serem executados
                # par[2] : tempo de simulação em ns
                par = line.rstrip().split()
                name = par[0][:-5]
                sTime = int(par[2])
                mif = "bin/hack/"+name+".mif"

                # verifica se arquivo existe
                if os.path.isfile(mif):
                    # simulate
                    for test in range(0, int(par[1])):
                        ramIn = "tests/" + name + "/" + name +"{}".format(test)+ "_in.mif"
                        ramTest = "tests/" + name + "/" + name +"{}".format(test)+ "_tst.mif"

                        RAM = [0] * (16*1024+4800+2)
                        ROM = [0] * 32*1024
                        #Import initial conditions from file
                        file_in = open(mif,"r")
                        Lines_in = file_in.readlines() 
                        file_in.close()
                        
                        for l in Lines_in:
                            if ":" in l:
                                no_line = int( l.split(":")[0].strip() )
                                value = int( l.split(":")[1].replace(";", "").strip(),2 )
                                ROM[no_line] = value 

                        file_in = open(ramIn,"r")
                        Lines_in = file_in.readlines() 
                        file_in.close()
                        
                        for l in Lines_in:
                            if ":" in l:
                                no_line = int( l.split(":")[0].strip() )
                                value = int( l.split(":")[1].replace(";", "").strip(),2 )
                                RAM[no_line] = value  

                        #### novo CPU ####
                        regA = np.uint16(0)
                        regD = np.uint16(0)
                        regPC = np.uint16(0)

                        for i in range( sTime ):
                            instruction = ROM[regPC]
                            instruction = '{0:018b}'.format(instruction)
                            regPC += 1

                            if instruction[0] == '0':
                                regA = np.uint16(int(instruction[2:],2))
                            else:
                                if instruction[4] == '0':
                                    resultado = alu(regD,regA, instruction[5:11])
                                else:
                                    resultado = alu(regD,RAM[regA], instruction[5:11])
                                if instruction[12] == '1':
                                    RAM[regA] = np.uint16(resultado)
                                if instruction[13] == '1':
                                    regD = np.uint16(resultado)
                                if instruction[14] == '1':
                                    regA = np.uint16(resultado)
                                if (instruction[15] == '1') and (resultado >= 32768):
                                    regPC = regA
                                if (instruction[16] == '1') and (resultado == 0):
                                    regPC = regA
                                if (instruction[17] == '1') and (resultado < 32768) and (resultado > 0):
                                    regPC = regA

                        #Verification final results
                        file_in = open(ramTest,"r")
                        Lines_in = file_in.readlines() 
                        file_in.close()

                        for l in Lines_in:
                            if ":" in l:
                                no_line = int( l.split(":")[0].strip() )
                                value = int( l.split(":")[1].replace(";", "").strip(),2 )

                                condition = (RAM[no_line] == value)
                                if not condition:
                                    print("Error in test " + name + "{}".format(test))
                                    print("Expected value RAM[" + str(no_line) + "]: " + "{0:016b}".format(value) + " Obtained value RAM[" + str(no_line) + "]: " + "{0:016b}".format(int(RAM[no_line])) )
                                    print( 'Test {:15s}: '.format(name + "{}".format(test)) + colored('Failed', 'red'))
                                    erro = 1
                                else:
                                    print( 'Test {:15s}: '.format(name + "{}".format(test)) + colored('Passed', 'green'))
    
    if erro == 1:
        assert False
    print("===================================================")
