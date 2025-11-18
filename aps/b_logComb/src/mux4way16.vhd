library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4way16 is
    port ( 
        a   : in  STD_LOGIC_VECTOR(15 downto 0);
        b   : in  STD_LOGIC_VECTOR(15 downto 0);
        c   : in  STD_LOGIC_VECTOR(15 downto 0);
        d   : in  STD_LOGIC_VECTOR(15 downto 0);
        sel : in  STD_LOGIC_VECTOR(1 downto 0);
        q   : out STD_LOGIC_VECTOR(15 downto 0)
    );
end entity;

architecture rtl of mux4way16 is
begin
    q <= a when sel = "00" else
         b when sel = "01" else
         c when sel = "10" else
         d; -- sel = "11"
end architecture;
