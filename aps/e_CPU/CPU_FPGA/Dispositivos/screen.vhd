LIBRARY ieee;
USE ieee.std_logic_1164.all;
use IEEE.NUMERIC_STD.ALL;

entity Screen is

   PORT(
        --Display
        INPUT        : IN  STD_LOGIC_VECTOR(15 downto 0);
        LOAD         : IN  STD_LOGIC;
        ADDRESS      : IN  STD_LOGIC_VECTOR(13 downto 0);
        LCD_INIT_OK  : OUT STD_LOGIC;

        -- Sistema
        CLK_SLOW     : IN  STD_LOGIC;
        CLK_FAST     : IN  STD_LOGIC;
        RST          : IN  STD_LOGIC;
        -- LCD EXTERNAL I/OS
        LCD_CS_N     : OUT   STD_LOGIC;
        LCD_D        : INOUT STD_LOGIC_VECTOR(15 downto 0);
        LCD_RD_N     : OUT   STD_LOGIC;
        LCD_RESET_N  : OUT   STD_LOGIC;
        LCD_RS       : OUT   STD_LOGIC;	-- (DCx) 0 : reg, 1: command
        LCD_WR_N     : OUT   STD_LOGIC
       );
end entity;


architecture arch of Screen is

	type Scr is array (0 to 8191) of STD_LOGIC_VECTOR(15 downto 0);
	signal ScrX16 : Scr := (others => (others => '0'));

begin
	process(CLK_FAST)
		--file out_file : text;
        	--variable out_line : line;
        	variable cache2: Scr := ScrX16;     	

	begin
		if rising_edge(CLK_FAST) then
			if LOAD = '1' then
				cache2( (to_integer(unsigned( ADDRESS ))  )  ) := INPUT;
			end if;
			--LCD_D <= cache( (to_integer(unsigned( ADDRESS ))  )  );
			
			
			--file_open(out_file, "/home/eu/RAM4K.tmp", WRITE_MODE);				
			--for addr in 0 to 4095 loop
			--	write(out_line, cache( addr  )   );
            		--	writeline(out_file, out_line);
            		--end loop;
            		--file_close(out_file); 

          	end if;
          	
	end process;
	
	LCD_D <= INPUT;

end architecture;
