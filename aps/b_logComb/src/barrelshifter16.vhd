library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.ALL;

entity barrelshifter16 is
    port ( 
        a    : in  STD_LOGIC_VECTOR(15 downto 0);
        dir  : in  STD_LOGIC;
        size : in  STD_LOGIC_VECTOR(2 downto 0);
        q    : out STD_LOGIC_VECTOR(15 downto 0)
    );
end entity;

architecture rtl of barrelshifter16 is
begin
    process(a, dir, size)
    begin
        if dir = '0' then
            q <= std_logic_vector(shift_left(unsigned(a), to_integer(unsigned(size))));
        else
            q <= std_logic_vector(shift_right(unsigned(a), to_integer(unsigned(size))));
        end if;
    end process;
end architecture;
