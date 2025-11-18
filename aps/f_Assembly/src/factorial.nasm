; Arquivo: Factorial.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Calcula o fatorial do número em R0 e armazena o valor em R1.


leaw   $0, %A
movw   (%A), %D
leaw   $1, %A
movw   $1, (%A)
leaw   $2, %A
movw   %D, (%A)
leaw   $2, %A
movw   (%A), %D
leaw   $fact_end, %A
je     %D
nop



fact_loop:
leaw   $1, %A
movw   (%A), %D
leaw   $4, %A
movw   %D, (%A)
leaw   $2, %A
movw   (%A), %D
leaw   $5, %A
movw   %D, (%A)
leaw   $3, %A
movw   $0, (%A)


mul_loop:
leaw   $5, %A
movw   (%A), %D
leaw   $mul_done, %A
je     %D
nop
decw   %D
leaw   $5, %A
movw   %D, (%A)
leaw   $3, %A
movw   (%A), %D
leaw   $4, %A
addw   (%A), %D, %D
leaw   $3, %A
movw   %D, (%A)
leaw   $mul_loop, %A
jmp
nop


mul_done:
leaw   $3, %A
movw   (%A), %D
leaw   $1, %A
movw   %D, (%A)
leaw   $2, %A
movw   (%A), %D
decw   %D
leaw   $2, %A
movw   %D, (%A)
leaw   $2, %A
movw   (%A), %D
leaw   $fact_loop, %A
jne     %D
nop

fact_end:
leaw   $fact_end, %A
jmp
nop