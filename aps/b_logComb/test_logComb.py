from cocotb_test.simulator import run
import pytest
import os

#from telemetry import telemetryMark
#pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)
   
#@pytest.mark.telemetry_files(source('and16.vhd'))
def test_and16():
    run(vhdl_sources=[source("and16.vhd")], toplevel="and16", module="logComb_cocotb" , testcase='tb_and16', toplevel_lang="vhdl")

#@pytest.mark.telemetry_files(source('or16.vhd'))
def test_or16():
    run(vhdl_sources=[source("or16.vhd")], toplevel="or16", module="logComb_cocotb" , testcase='tb_or16', toplevel_lang="vhdl")
    
#@pytest.mark.telemetry_files(source('not16.vhd'))
def test_not16():
    run(vhdl_sources=[source("not16.vhd")], toplevel="not16", module="logComb_cocotb" , testcase='tb_not16', toplevel_lang="vhdl")

#@pytest.mark.telemetry_files(source('or8way.vhd'))
def test_or8way():
    run(vhdl_sources=[source("or8way.vhd")], toplevel="or8way", module="logComb_cocotb" , testcase='tb_or8way', toplevel_lang="vhdl")    

#@pytest.mark.telemetry_files(source('nor8way.vhd'))
def test_nor8way():
    run(vhdl_sources=[source("nor8way.vhd")], toplevel="nor8way", module="logComb_cocotb" , testcase='tb_nor8way', toplevel_lang="vhdl")  

#3@pytest.mark.telemetry_files(source('barrelshifter16.vhd'))
def test_barrelshifter16():
    run(vhdl_sources=[source("barrelshifter16.vhd")], toplevel="barrelshifter16", module="logComb_cocotb" , testcase='tb_barrelshifter16', toplevel_lang="vhdl")  
    
#@pytest.mark.telemetry_files(source('dmux2way.vhd'))
def test_dmux2way():
    run(vhdl_sources=[source("dmux2way.vhd")], toplevel="dmux2way", module="logComb_cocotb" , testcase='tb_dmux2way', toplevel_lang="vhdl")  
  
#@pytest.mark.telemetry_files(source('dmux4way.vhd'))
def test_dmux4way():
    run(vhdl_sources=[source("dmux4way.vhd")], toplevel="dmux4way", module="logComb_cocotb" , testcase='tb_dmux4way', toplevel_lang="vhdl")  

#@pytest.mark.telemetry_files(source('dmux8way.vhd'))
def test_dmux8way():
    run(vhdl_sources=[source("dmux8way.vhd")], toplevel="dmux8way", module="logComb_cocotb" , testcase='tb_dmux8way', toplevel_lang="vhdl")
    
#@pytest.mark.telemetry_files(source('mux2way.vhd'))
def test_mux2way():
    run(vhdl_sources=[source("mux2way.vhd")], toplevel="mux2way", module="logComb_cocotb" , testcase='tb_mux2way', toplevel_lang="vhdl")
    
#@pytest.mark.telemetry_files(source('mux4way.vhd'))
def test_mux4way():
    run(vhdl_sources=[source("mux4way.vhd")], toplevel="mux4way", module="logComb_cocotb" , testcase='tb_mux4way', toplevel_lang="vhdl")                     

#@pytest.mark.telemetry_files(source('mux8way.vhd'))
def test_mux8way():
    run(vhdl_sources=[source("mux8way.vhd")], toplevel="mux8way", module="logComb_cocotb" , testcase='tb_mux8way', toplevel_lang="vhdl") 
    
#@pytest.mark.telemetry_files(source('mux16.vhd'))
def test_mux16():
    run(vhdl_sources=[source("mux16.vhd")], toplevel="mux16", module="logComb_cocotb" , testcase='tb_mux16', toplevel_lang="vhdl")                       
        
#@pytest.mark.telemetry_files(source('mux4way16.vhd'))
def test_mux4way16():
    run(vhdl_sources=[source("mux4way16.vhd")], toplevel="mux4way16", module="logComb_cocotb" , testcase='tb_mux4way16', toplevel_lang="vhdl")  
    
#@pytest.mark.telemetry_files(source('mux8way16.vhd'))
def test_mux8way16():
    run(vhdl_sources=[source("mux8way16.vhd")], toplevel="mux8way16", module="logComb_cocotb" , testcase='tb_mux8way16', toplevel_lang="vhdl")  
        
#@pytest.mark.telemetry_files(source('detectordemoedas.vhd'))
def test_detector_de_moedas():
    run(vhdl_sources=[source("detectordemoedas.vhd")], toplevel="detectordemoedas", module="logComb_cocotb" , testcase='tb_detector_de_moedas', toplevel_lang="vhdl")          
 
#@pytest.mark.telemetry_files(source('circuito.vhd'))
def test_circuito():
    run(vhdl_sources=[source("circuito.vhd")], toplevel="circuito", module="logComb_cocotb" , testcase='tb_circuito', toplevel_lang="vhdl") 
    
#@pytest.mark.telemetry_files(source('impressora.vhd'))
def test_impressora():
    run(vhdl_sources=[source("impressora.vhd")], toplevel="impressora", module="logComb_cocotb" , testcase='tb_impressora', toplevel_lang="vhdl") 
    
#@pytest.mark.telemetry_files(source('sevenseg.vhd'))
def test_sevenseg():
    run(vhdl_sources=[source("sevenseg.vhd")], toplevel="sevenseg", module="logComb_cocotb" , testcase='tb_sevenseg', toplevel_lang="vhdl")      
    

if __name__ == "__main__":
    test_and16()
    test_or16()
    test_not16()
    test_or8way()
    test_nor8way()
    test_barrelshifter16()
    test_dmux2way()
    test_dmux4way()
    test_dmux8way()
    test_mux4way16()
    test_mux8way16()
    test_detector_de_moedas()
    test_circuito()
    test_impressora()
    test_sevenseg()
