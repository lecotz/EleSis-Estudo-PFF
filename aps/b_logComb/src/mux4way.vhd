library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux4way is
    port ( 
        a   : in  STD_LOGIC;
        b   : in  STD_LOGIC;
        c   : in  STD_LOGIC;
        d   : in  STD_LOGIC;
        sel : in  STD_LOGIC_VECTOR(1 downto 0);
        q   : out STD_LOGIC
    );
end entity;

architecture rtl of mux4way is
begin
    q <= a when sel = "00" else
         b when sel = "01" else
         c when sel = "10" else
         d; -- sel = "11"
end architecture;
