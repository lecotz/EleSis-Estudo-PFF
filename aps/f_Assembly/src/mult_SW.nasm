; Arquivo: mult_SW.nasm
; Curso: Elementos de Sistemas
; Criado por: Renan Trevisoli
; Data: 16/04/25
;
; Realiza a multiplicação SW(9 downto 5)*SW(4 downto 0)
; e mostra o resultado nos LEDs
; exemplo: "0101100110" => 0d11*0d6 => 0d66 => "0001000010"

leaw   $21185, %A
movw   (%A), %D
leaw   $7,     %A
movw   %D,     (%A)
leaw   $2,     %A
movw   $0,     (%A)

loop_divsw:
leaw   $7,     %A
movw   (%A), %D
leaw   $32,    %A
subw   %D, %A, %D
leaw   $end_divsw, %A
jl     %D
nop
leaw   $7,     %A
movw   %D,     (%A)
leaw   $2,     %A
movw   (%A), %D
incw   %D
movw   %D,     (%A)
leaw   $loop_divsw, %A
jmp
nop

end_divsw:
leaw   $7,     %A
movw   (%A), %D
leaw   $3,     %A
movw   %D,     (%A)
leaw   $2,     %A
movw   (%A), %D
leaw   $5,     %A
movw   %D,     (%A)
leaw   $4,     %A
movw   $0,     (%A)

loop_mulsw:
leaw   $3,     %A
movw   (%A), %D
leaw   $end_mulsw, %A
je     %D
nop
decw   %D
leaw   $3,     %A
movw   %D,     (%A)
leaw   $4,     %A
movw   (%A), %D
leaw   $5,     %A
addw   (%A), %D, %D
leaw   $4,     %A
movw   %D,     (%A)
leaw   $loop_mulsw, %A
jmp
nop

end_mulsw:
leaw   $4,     %A
movw   (%A), %D
leaw   $21184, %A
movw   %D,     (%A)
leaw   $end_mulsw, %A
jmp
nop