library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.all;

entity TopLevel is
	port(
		SW    : in  std_logic_vector(9 downto 0);
		KEY   : in  std_logic_vector(3 downto 0);
		LEDR  : out std_logic_vector(9 downto 0);
		HEX0  : out std_logic_vector(6 downto 0); -- 7seg0
		HEX1  : out std_logic_vector(6 downto 0); -- 7seg1
		HEX2  : out std_logic_vector(6 downto 0); -- 7seg2
		HEX3  : out std_logic_vector(6 downto 0)  -- 7seg3
	);
end entity;

architecture rtl of TopLevel is

    -- Declaração dos componentes
    component sevenseg is
        Port (
            bcd : in  STD_LOGIC_VECTOR(3 downto 0);
            leds : out STD_LOGIC_VECTOR(6 downto 0)
        );
    end component;


    component PC is
        Port(
            clock     : in  STD_LOGIC;
            increment : in  STD_LOGIC;
            load      : in  STD_LOGIC;
            reset     : in  STD_LOGIC;
            input     : in  STD_LOGIC_VECTOR(15 downto 0);
            output    : out STD_LOGIC_VECTOR(15 downto 0) 
        );
    end component;

    -- Sinais auxiliares
    signal clock, clear, set : std_logic;
    signal saida_ram : std_logic_vector(15 downto 0);

begin

    -- Inversão do botão (ativo em nível baixo)
    clock <= not KEY(0);

    -- Instância do PC
    u1 : pc port map (
        clock  => clock,
        increment => '1',
        load => SW(2),
        reset => SW(1),
        input   => "0000000000000100",  -- dado de entrada fixo
        output  => saida_ram
    );

    -- Conversão dos 4 grupos de 4 bits para os displays HEX0 a HEX3
    u2 : sevenseg port map (
        bcd => saida_ram(3 downto 0),
        leds => HEX0
    );

    u3 : sevenseg port map (
        bcd => saida_ram(7 downto 4),
        leds => HEX1
    );

    u4 : sevenseg port map (
        bcd => saida_ram(11 downto 8),
        leds => HEX2
    );

    u5 : sevenseg port map (
        bcd => saida_ram(15 downto 12),
        leds => HEX3
    );

end rtl;