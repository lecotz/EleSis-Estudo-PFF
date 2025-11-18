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

nasm = [pwd+"/src/", pwd+"/src/examples/"]
hack = pwd+"/bin/hack/"

print("-------------------------")
print("-  Inicio      ")
print("-------------------------")
error, log = assembler.compileAll("jar/Z01-Assembler.jar", nasm, hack)

if error > 0:
    print("Finalizado com erro")
else:
    print("Finalizado sem erros de compilação")
#sys.exit(compileAllNotify(error, log))
