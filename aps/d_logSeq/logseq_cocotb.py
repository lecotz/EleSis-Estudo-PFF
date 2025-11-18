# Adapted from https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/test_my_design.py

import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock
        
        
@cocotb.test()
async def tb_binarydigit(dut):

    ininput =   [0, 1, 1, 0]
    inload  =   [1, 0, 1, 0]
    outoutput = [0, 0, 1, 1]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_flipflopd(dut):

    ind      = [0, 1, 0, 0, 1, 1]
    inpreset = [0, 0, 1, 0, 0, 0]
    inclear  = [1, 0, 0, 0, 0, 1]
    outq     = [0, 1, 1, 0, 1, 0]
    
    clock = Clock(dut.clock, len(ind), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ind)):
        dut.d.value = ind[i]
        dut.preset.value = inpreset[i]
        dut.clear.value = inclear[i]

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_pc(dut):

    inincrement = [1, 1, 0, 0, 0, 1]
    inload      = [0, 0, 0, 0, 1, 0]
    inreset     = [0, 0, 0, 1, 0, 0]
    ininput     = [0x0000, 0x0000, 0x5555, 0x5555, 0x5555, 0x0000]
    outoutput   = [0x0001, 0x0002, 0x0002, 0x0000, 0x5555, 0x5556]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.increment.value = inincrement[i]
        dut.load.value = inload[i]
        dut.reset.value = inreset[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_register8(dut):

    ininput =   [0b00100001, 0b11011110, 0b11011110, 0b11111111]
    inload  =   [1, 0, 1, 0]
    outoutput = [0b00100001, 0b00100001, 0b11011110, 0b11011110]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:08b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_register16(dut):

    ininput =   [0x0F0F, 0x5555, 0x5555, 0xAAAA]
    inload  =   [1, 0, 1, 0]
    outoutput = [0x0F0F, 0x0F0F, 0x5555, 0x5555]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_register32(dut):

    ininput =   [0x0F0F0F0F, 0x55555555, 0x55555555, 0xAAAAAAAA]
    inload  =   [1, 0, 1, 0]
    outoutput = [0x0F0F0F0F, 0x0F0F0F0F, 0x55555555, 0x55555555]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:032b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_register64(dut):

    ininput =   [0x0F0F0F0F0F0F0F0F, 0x5555555555555555, 0x5555555555555555, 0xAAAAAAAAAAAAAAAA]
    inload  =   [1, 0, 1, 0]
    outoutput = [0x0F0F0F0F0F0F0F0F, 0x0F0F0F0F0F0F0F0F, 0x5555555555555555, 0x5555555555555555]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:032b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_ram8(dut):

    ininput =   [0x5555, 0xAAAA, 0xAAAA, 0xFFFF, 0xFFFF, 0xF0F0]
    inload  =   [     1,      0,      1,      0,      1,      0]
    inaddress = [ 0b000,  0b000,  0b010,  0b010,  0b011,  0b011]
    outoutput = [0x5555, 0x5555, 0xAAAA, 0xAAAA, 0xFFFF, 0xFFFF]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]
        dut.address.value = inaddress[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_ram64(dut):

    ininput =   [0x0000, 0xAAAA, 0xAAAA, 0xFFFF, 0xFFFF, 0xFFFF, 0xF0F0]
    inload  =   [     1,      0,      1,      0,      0,      1,      0]
    inaddress = [  0x00,   0x00,   0x03,   0x00,   0x03,   0x3A,   0x3A]
    outoutput = [0x0000, 0x0000, 0xAAAA, 0x0000, 0xAAAA, 0xFFFF, 0xFFFF]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]
        dut.address.value = inaddress[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_ram512(dut):

    ininput =   [0x0000, 0xAAAA, 0xAAAA, 0xFFFF, 0xFFFF, 0xFFFF, 0xF0F0]
    inload  =   [     1,      0,      1,      0,      0,      1,      0]
    inaddress = [ 0x000,  0x000,  0x003,  0x000,  0x003,  0x13A,  0x13A]
    outoutput = [0x0000, 0x0000, 0xAAAA, 0x0000, 0xAAAA, 0xFFFF, 0xFFFF]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]
        dut.address.value = inaddress[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_ram4k(dut):

    ininput =   [0x0000, 0xAAAA, 0xAAAA, 0xFFFF, 0xFFFF, 0xFFFF, 0xF0F0]
    inload  =   [     1,      0,      1,      0,      0,      1,      0]
    inaddress = [ 0x000,  0x000,  0x103,  0x000,  0x103,  0x83A,  0x83A]
    outoutput = [0x0000, 0x0000, 0xAAAA, 0x0000, 0xAAAA, 0xFFFF, 0xFFFF]
    
    clock = Clock(dut.clock, len(ininput), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(ininput)):
        dut.input.value = ininput[i]
        dut.load.value = inload[i]
        dut.address.value = inaddress[i]

        await FallingEdge(dut.clock)

        condition = (dut.output.value == outoutput[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:016b}".format(outoutput[i]) + " Obtained value: " + str(dut.output.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_counterdown(dut):

    outq = [0b111, 0b110, 0b101, 0b100, 0b011, 0b010, 0b001, 0b000]
    
    clock = Clock(dut.clock, len(outq), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(outq)):

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i])
        if not condition:
            dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_flipflopt(dut):

    in_t    = [0, 0, 1, 1, 1]
    outq    = [0, 0, 1, 0, 1]
    outnotq = [1, 1, 0, 1, 0]
    
    clock = Clock(dut.clock, len(in_t), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(in_t)):
        dut.t.value = in_t[i]

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i] and dut.notq.value == outnotq[i])
        if not condition:
            if not dut.q.value == outq[i]:
                dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            if not dut.notq.value == outnotq[i]:
                dut._log.error("Expected value: " + "{0:b}".format(outnotq[i]) + " Obtained value: " + str(dut.notq.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_flipflopjk(dut):

    inJ     = [0, 0, 1, 1, 1]
    inK     = [0, 1, 0, 1, 1]
    outq    = [0, 0, 1, 0, 1]
    outnotq = [1, 1, 0, 1, 0]
    
    clock = Clock(dut.clock, len(inJ), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.clock)
    for i in range(len(inJ)):
        dut.J.value = inJ[i]
        dut.K.value = inK[i]

        await FallingEdge(dut.clock)

        condition = (dut.q.value == outq[i] and dut.notq.value == outnotq[i])
        if not condition:
            if not dut.q.value == outq[i]:
                dut._log.error("Expected value: " + "{0:b}".format(outq[i]) + " Obtained value: " + str(dut.q.value) )
            if not dut.notq.value == outnotq[i]:
                dut._log.error("Expected value: " + "{0:b}".format(outnotq[i]) + " Obtained value: " + str(dut.notq.value) )
            assert condition, "Error in test {0}!".format(i) 