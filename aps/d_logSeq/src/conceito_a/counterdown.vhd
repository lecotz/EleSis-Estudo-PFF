-- Elementos de Sistemas
-- CounterDown.vhd

library ieee;
use ieee.std_logic_1164.all;

entity CounterDown is
	port(
		clock:  in std_logic;
		q:      out std_logic_vector(2 downto 0) :=(others => '0')
	);
end entity;

architecture arch of CounterDown is

	component FlipFlopT is
	port(
		clock:  in std_logic;
		t:      in std_logic;
		q:      out std_logic:= '0';
		notq:   out std_logic:= '1'
	);
	end component;

	signal ck, q0, q1, q2: STD_LOGIC;

  	signal t0, t1, t2 : std_logic;

begin

  	ck <= clock;

	t0 <= '1';
	t1 <= not q0;
	t2 <= (not q0) and (not q1);

	FF0: FlipFlopT
		port map(
		clock => ck,
		t     => t0,
		q     => q0,
		notq  => open
		);

	FF1: FlipFlopT
		port map(
		clock => ck,
		t     => t1,
		q     => q1,
		notq  => open
		);

	FF2: FlipFlopT
		port map(
		clock => ck,
		t     => t2,
		q     => q2,
		notq  => open
		);

  	q <= q2 & q1 & q0;

end architecture;
