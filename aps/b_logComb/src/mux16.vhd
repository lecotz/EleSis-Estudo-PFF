library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux16 is
    port ( 
        a   : in  STD_LOGIC_VECTOR(15 downto 0);
        b   : in  STD_LOGIC_VECTOR(15 downto 0);
        sel : in  STD_LOGIC;
        q   : out STD_LOGIC_VECTOR(15 downto 0)
    );
end entity;

architecture rtl of mux16 is
begin
    q <= a when sel = '0' else b;
end architecture;
