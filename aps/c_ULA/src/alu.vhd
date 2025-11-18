-- Elementos de Sistemas
-- by Luciano Soares
-- ALU.vhd

-- Unidade Lógica Aritmética (ULA)
-- Recebe dois valores de 16bits e
-- calcula uma das seguintes funções:
-- X+y, x-y, y-x, 0, 1, -1, x, y, -x, -y,
-- X+1, y+1, x-1, y-1, x&y, x|y
-- De acordo com os 6 bits de entrada denotados:
-- zx, nx, zy, ny, f, no.
-- Também calcula duas saídas de 1 bit:
-- Se a saída == 0, zr é definida como 1, senão 0;
-- Se a saída <0, ng é definida como 1, senão 0.
-- a ULA opera sobre os valores, da seguinte forma:
-- se (zx == 1) então x = 0
-- se (nx == 1) então x =! X
-- se (zy == 1) então y = 0
-- se (ny == 1) então y =! Y
-- se (f == 1) então saída = x + y
-- se (f == 0) então saída = x & y
-- se (no == 1) então saída = !saída
-- se (out == 0) então zr = 1
-- se (out <0) então ng = 1

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ALU is
	port (
			x,y:   in STD_LOGIC_VECTOR(15 downto 0); -- entradas de dados da ALU
			zx:    in STD_LOGIC;                     -- zera a entrada x
			nx:    in STD_LOGIC;                     -- inverte a entrada x
			zy:    in STD_LOGIC;                     -- zera a entrada y
			ny:    in STD_LOGIC;                     -- inverte a entrada y
			f:     in STD_LOGIC;                     -- se 0 calcula x & y, senão x + y
			no:    in STD_LOGIC;                     -- inverte o valor da saída
			zr:    out STD_LOGIC;                    -- setado se saída igual a zero
			ng:    out STD_LOGIC;                    -- setado se saída é negativa
			saida: out STD_LOGIC_VECTOR(15 downto 0) -- saída de dados da ALU
	);
end entity;

architecture estrut of ALU is
  -- sinais internos
  signal x_z, y_z   : STD_LOGIC_VECTOR(15 downto 0);
  signal x_n, y_n   : STD_LOGIC_VECTOR(15 downto 0);
  signal and_out    : STD_LOGIC_VECTOR(15 downto 0);
  signal add_out    : STD_LOGIC_VECTOR(15 downto 0);
  signal f_out      : STD_LOGIC_VECTOR(15 downto 0);
  signal out_final  : STD_LOGIC_VECTOR(15 downto 0);
begin
  -- ZX/ZY: zerar condicionalmente (zerador16: z, a, y)
  u_zx: entity work.zerador16
    port map(
      z => zx,
      a => x,
      y => x_z
    );

  u_zy: entity work.zerador16
    port map(
      z => zy,
      a => y,
      y => y_z
    );

  -- NX/NY: inverter condicionalmente (inversor16: z, a, y)
  u_nx: entity work.inversor16
    port map(
      z => nx,
      a => x_z,
      y => x_n
    );

  u_ny: entity work.inversor16
    port map(
      z => ny,
      a => y_z,
      y => y_n
    );

  -- Operações básicas
  u_and: entity work.and16
    port map(
      a => x_n,
      b => y_n,
      q => and_out
    );

  u_add: entity work.add16
    port map(
      a => x_n,
      b => y_n,
      q => add_out
    );

  -- f: 0 = AND, 1 = ADD (mux16: a, b, sel, q)
  u_f: entity work.mux16
    port map(
      a   => and_out,
      b   => add_out,
      sel => f,
      q   => f_out
    );

  -- no: inverte saída final (reusa inversor16)
  u_no: entity work.inversor16
    port map(
      z => no,
      a => f_out,
      y => out_final
    );

  -- saída
  saida <= out_final;

  -- flags (comparador16: a, zr, ng)
  u_cmp: entity work.comparador16
    port map(
      a  => out_final,
      zr => zr,
      ng => ng
    );
end architecture;


