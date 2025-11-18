-- Elementos de Sistemas
-- Ram16K.vhd


LIBRARY ieee;
USE ieee.std_logic_1164.all;
use IEEE.NUMERIC_STD.ALL;


ENTITY RAM16K IS
	PORT
	(
		address		: IN STD_LOGIC_VECTOR (13 DOWNTO 0);
		clock		: IN STD_LOGIC  := '1';
		data		: IN STD_LOGIC_VECTOR (15 DOWNTO 0);
		wren		: IN STD_LOGIC ;
		q		: OUT STD_LOGIC_VECTOR (15 DOWNTO 0)
	);
END RAM16K;


architecture arch of RAM16K is
	type MEM is array (0 to 16383) of STD_LOGIC_VECTOR(15 downto 0);
	signal MEM16kX16 : MEM := (others => (others => '0'));
begin
	process(clock)
		--file out_file : text;
        	--variable out_line : line;
        	variable cache: MEM := MEM16kX16;     	

	begin
		if rising_edge(clock) then
			if wren = '1' then
				cache( (to_integer(unsigned( address )))  ) := data;
			end if;
			q <= cache( (to_integer(unsigned( address )))  );
			
			
			--file_open(out_file, "/home/eu/RAM4K.tmp", WRITE_MODE);				
			--for addr in 0 to 4095 loop
			--	write(out_line, cache( addr  )   );
            		--	writeline(out_file, out_line);
            		--end loop;
            		--file_close(out_file); 

          	end if;
          	
	end process;

end architecture;
