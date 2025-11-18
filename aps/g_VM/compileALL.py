#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Curso de Elementos de Sistemas
# Desenvolvido por: Rafael Corsi <rafael.corsi@insper.edu.br>
#
# Adaptado de :     Pedro Cunial   <pedrocc4@al.insper.edu.br>
#                   Luciano Soares <lpsoares@insper.edu.br>
# Data de criação: 07/2017

######################################################################
# Tools
######################################################################
from os.path import dirname, abspath
from jar import assembler

pwd = dirname(abspath(__file__))

vmDir = [pwd+"/src/vm/", pwd+"/src/examples/"]
nasm = pwd+"/bin/nasm/"
hack = pwd+"/bin/hack/"

assembler.clearbin(nasm)
assembler.clearbin(hack)

print("------------------------------")
print("- Translating src files       ")
print("- to H-VM/bin/nasm/ ")
print("------------------------------")
assembler.vmtranslator(False, vmDir, nasm, "jar/Z01-VMTranslator.jar")

print("-------------------------")
print("- Assembling files default.... " )
print("-------------------------")
error, log = assembler.compileAll("jar/Z01-Assembler.jar", [nasm], hack)


nasm = pwd+"/bin/nasm_group/"
hack = pwd+"/bin/hack_group/"

assembler.clearbin(nasm)
assembler.clearbin(hack)

print("------------------------------")
print("- Translating src files       ")
print("- to H-VM/bin/nasm_group/ ")
print("------------------------------")
assembler.vmtranslator(False, vmDir, nasm, "VMtranslator/Z01-VMTranslator.jar")

print("-------------------------")
print("- Assembling files group.... " )
print("-------------------------")
error, log = assembler.compileAll("jar/Z01-Assembler.jar", [nasm], hack)

if error > 0:
    print("Finalizado com erro")
else:
    print("Finalizado sem erros de compilação")
#sys.exit(compileAllNotify(error, log))
