from cocotb_test.simulator import run
import pytest
import os

#from telemetry import telemetryMark
#pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)


#@pytest.mark.telemetry_files(source('zerador16.vhd'))
def test_zerador16():
    run(vhdl_sources=[source("zerador16.vhd")], toplevel="zerador16", module="ula_cocotb" , testcase='tb_zerador16', toplevel_lang="vhdl")


#@pytest.mark.telemetry_files(source('inversor16.vhd'))
def test_inversor16():
    run(vhdl_sources=[source("inversor16.vhd")], toplevel="inversor16", module="ula_cocotb" , testcase='tb_inversor16', toplevel_lang="vhdl")


#@pytest.mark.telemetry_files(source('comparador16.vhd'))
def test_comparador16():
    run(vhdl_sources=[source("comparador16.vhd")], toplevel="comparador16", module="ula_cocotb" , testcase='tb_comparador16', toplevel_lang="vhdl")



#@pytest.mark.telemetry_files(source('fulladder.vhd'))
def test_fulladder():
    run(vhdl_sources=[source("fulladder.vhd")], toplevel="fulladder", module="ula_cocotb" , testcase='tb_fulladder', toplevel_lang="vhdl")


#@pytest.mark.telemetry_files(source('halfadder.vhd'))
def test_halfadder():
    run(vhdl_sources=[source("halfadder.vhd")], toplevel="halfadder", module="ula_cocotb" , testcase='tb_halfadder', toplevel_lang="vhdl")


#@pytest.mark.telemetry_files(source('add16.vhd'), source('fulladder.vhd'))
def test_add16():
    run(vhdl_sources=[source("add16.vhd"), source("fulladder.vhd")], toplevel="add16", module="ula_cocotb" , testcase='tb_add16', toplevel_lang="vhdl")


#@pytest.mark.telemetry_files(source('inc16.vhd'), source('add16.vhd'), source('fulladder.vhd'))
def test_inc16():
    run(vhdl_sources=[source("inc16.vhd"), source('add16.vhd'), source('fulladder.vhd')], toplevel="inc16", module="ula_cocotb" , testcase='tb_inc16', toplevel_lang="vhdl")


#@pytest.mark.telemetry_files(source("alu.vhd"),source("zerador16.vhd"), source("inversor16.vhd"), source("add16.vhd"), source("fulladder.vhd"), source("../../b_logComb/src/and16.vhd"), source("comparador16.vhd"), source("../../b_logComb/src/mux16.vhd"))
def test_alu():
    run(vhdl_sources=[source("alu.vhd"),source("zerador16.vhd"), source("inversor16.vhd"), source("add16.vhd"), source("fulladder.vhd"), source("../../b_logComb/src/and16.vhd"), source("comparador16.vhd"), source("../../b_logComb/src/mux16.vhd")], toplevel="alu", module="ula_cocotb" , testcase='tb_alu', toplevel_lang="vhdl")


  
if __name__ == "__main__":
    test_zerador16()
    test_inversor16()
    test_comparador16()
    test_fulladder()
    test_halfadder()
    test_add16()
    test_inc16()
    test_alu()
