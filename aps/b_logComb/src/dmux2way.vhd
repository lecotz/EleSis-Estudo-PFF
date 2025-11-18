library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity dmux2way is
    port ( 
        a   : in  STD_LOGIC;
        sel : in  STD_LOGIC;
        q0  : out STD_LOGIC;
        q1  : out STD_LOGIC
    );
end entity;

architecture rtl of dmux2way is
begin
    q0 <= a when sel = '0' else '0';
    q1 <= a when sel = '1' else '0';
end architecture;
