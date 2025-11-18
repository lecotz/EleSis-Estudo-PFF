library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.ALL;

entity detectordemoedas is
	port (
    Q,D,N : in  STD_LOGIC;
    cents     : out STD_LOGIC_VECTOR(4 downto 0));
end entity;

architecture arch of detectordemoedas is

begin
    cents <= "11001" when Q = '1' else
    "01010" when D = '1' else
    "00101" when N = '1' else
    "00000";
end architecture;
