# Adapted from https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/test_my_design.py

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def tb_add16(dut):

    inA = [0b0000000000000000, 0b0000000000000000, 0b1111111111111111, 0b1010101010101010, 0b0011110011000011, 0b0001001000110100, 0b0000000000000001]
    inB = [0b0000000000000001, 0b1111111111111111, 0b1111111111111111, 0b0101010101010101, 0b0000111111110000, 0b1001100001110110, 0b1111111111111111]
    outq =[0b0000000000000001, 0b1111111111111111, 0b1111111111111110, 0b1111111111111111, 0b0100110010110011, 0b1010101010101010, 0b0000000000000000]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_halfadder(dut):

    inA =     [0, 0, 1, 1]
    inB =     [0, 1, 0, 1]
    outsoma = [0, 1, 1, 0]
    outvaium= [0, 0, 0, 1]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.soma.value == outsoma[i] and dut.vaium.value == outvaium[i])
        if not condition:
            if not (dut.soma.value == outsoma[i]):
                dut._log.error("Expected value soma: " + "{0:b}".format(outsoma[i]) + " Obtained value soma: " + str(dut.soma.value) )
            if not (dut.vaium.value == outvaium[i]):
                dut._log.error("Expected value vaium: " + "{0:b}".format(outvaium[i]) + " Obtained value vaium: " + str(dut.vaium.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_fulladder(dut):

    inA =     [0, 0, 1, 1, 0, 0, 1, 1]
    inB =     [0, 1, 0, 1, 0, 1, 0, 1]
    inC =     [0, 0, 0, 0, 1, 1, 1, 1]
    outsoma = [0, 1, 1, 0, 1, 0, 0, 1]
    outvaium= [0, 0, 0, 1, 0, 1, 1, 1]

    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.c.value = inC[i]

        await Timer(1, units="ns")
        condition = (dut.soma.value == outsoma[i] and dut.vaium.value == outvaium[i])
        if not condition:
            if not (dut.soma.value == outsoma[i]):
                dut._log.error("Expected value soma: " + "{0:b}".format(outsoma[i]) + " Obtained value soma: " + str(dut.soma.value) )
            if not (dut.vaium.value == outvaium[i]):
                dut._log.error("Expected value vaium: " + "{0:b}".format(outvaium[i]) + " Obtained value vaium: " + str(dut.vaium.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")

@cocotb.test()
async def tb_inc16(dut):

    inA = [0b0000000000000000, 0b1111111111111111, 0b0000000000000101, 0b1111111111111011]
    outq =[0b0000000000000001, 0b0000000000000000, 0b0000000000000110, 0b1111111111111100]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_inversor16(dut):

    ina = [0x0000, 0x0000]
    inz = [0, 1]
    outy =[0x0000, 0xFFFF]
    
    for i in range(len(ina)):
        dut.a.value = ina[i]
        dut.z.value = inz[i]

        await Timer(1, units="ns")
        condition = (dut.y.value == outy[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outy[i]) + " Obtained value: " + str(dut.y.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_zerador16(dut):

    ina = [0xFFFF, 0xA5A5]
    inz = [1, 0]
    outy =[0x0000, 0xA5A5]
    
    for i in range(len(ina)):
        dut.a.value = ina[i]
        dut.z.value = inz[i]

        await Timer(1, units="ns")
        condition = (dut.y.value == outy[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outy[i]) + " Obtained value: " + str(dut.y.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_comparador16(dut):

    ina =   [0x0000, 0x8000, 0x5555]
    outzr = [1, 0, 0]
    outng = [0, 1, 0]
    
    for i in range(len(ina)):
        dut.a.value = ina[i]

        await Timer(1, units="ns")
        condition = (dut.zr.value == outzr[i] and dut.ng.value == outng[i])
        if not condition:
            if not (dut.zr.value == outzr[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outzr[i]) + " Obtained value: " + str(dut.zr.value) )
            if not (dut.ng.value == outng[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outng[i]) + " Obtained value: " + str(dut.ng.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")


@cocotb.test()
async def tb_alu(dut):

    inX =     [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000]
    inY =     [0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF]
    outsaida =[0x0000, 0x0001, 0xFFFF, 0x0000, 0xFFFF, 0xFFFF, 0x0000, 0x0000, 0x0001, 0x0001, 0x0000, 0xFFFF, 0xFFFE, 0xFFFF, 0x0001, 0xFFFF, 0x0000, 0xFFFF]
    inzx = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
    innx = [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1]
    inzy = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    inny = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1]
    inf  = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    inno = [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1]
    outng= [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
    outzr= [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    
    

    for i in range(len(inX)):
        dut.x.value = inX[i]
        dut.y.value = inY[i]
        dut.zx.value = inzx[i]
        dut.nx.value = innx[i]
        dut.zy.value = inzy[i]
        dut.ny.value = inny[i]
        dut.f.value =  inf[i]
        dut.no.value = inno[i]

        await Timer(1, units="ns")
        condition = (dut.saida.value == outsaida[i] and dut.zr.value == outzr[i] and dut.ng.value == outng[i])
        if not condition:
            if not (dut.saida.value == outsaida[i]):
                dut._log.error("Expected value: " + "{0:016b}".format(outsaida[i]) + " Obtained value: " + str(dut.saida.value) )
            if not (dut.zr.value == outzr[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outzr[i]) + " Obtained value: " + str(dut.zr.value) )
            if not (dut.ng.value == outng[i]):
                dut._log.error("Expected value: " + "{0:b}".format(outng[i]) + " Obtained value: " + str(dut.ng.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")

@cocotb.test()
async def tb_and16(dut):

    inA = [0b1111000011110000, 0b1010101010101010, 0b0101010101010101, 0b0000000000000000, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    inB = [0b0000111100001111, 0b0000000000000000, 0b0000000000000000, 0b1010101010101010, 0b0101010101010101, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    outq =[0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b0000000000000000, 0b1111111111111111, 0b0101010101010101, 0b1010101010101010]
    
    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")

@cocotb.test()
async def tb_mux16(dut):

    inA =   [0b1111000011110000, 0b0000000000000000, 0b1111000011110000, 0b0000000000000000]
    inB =   [0b0000000000000000, 0b1111000011110000, 0b0000000000000000, 0b1111000011110000]
    inSel = [0, 1, 1, 0]
    outq =  [0b1111000011110000, 0b1111000011110000, 0b0000000000000000, 0b0000000000000000]


    for i in range(len(inA)):
        dut.a.value = inA[i]
        dut.b.value = inB[i]
        dut.sel.value = inSel[i]

        await Timer(1, units="ns")
        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")