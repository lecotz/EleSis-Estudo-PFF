library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity not16 is
	port ( 
			a:   in  STD_LOGIC_VECTOR(15 downto 0);
			q:   out STD_LOGIC_VECTOR(15 downto 0));
end entity;

architecture arch of not16 is
begin
	
	q <=not a;

end architecture;

