; ------------------------------------------------------------
; Arquivo: Mod.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017
;
; Calcula o resto da divisão (modulus) entre RAM[0] por RAM[1]
; e armazena o resultado na RAM[2].
;
; 4  % 3 = 1
; 10 % 7 = 3
; ------------------------------------------------------------

INICIO:
leaw $0, %A          ; A = 0
movw (%A), %D        ; D = RAM[0]
leaw $3, %A          ; A = 3
movw %D, (%A)        ; RAM[3] = RAM[0]

LOOP:
leaw $3, %A          ; A = 3
movw (%A), %D        ; D = RAM[3]
leaw $1, %A          ; A = 1
subw %D, (%A), %D    ; D = RAM[3] - RAM[1]
leaw $FIM, %A        ; se D < 0, termina
jl
nop

leaw $3, %A
movw %D, (%A)        ; RAM[3] = RAM[3] - RAM[1]
leaw $LOOP, %A
jmp
nop

FIM:
leaw $3, %A          ; A = 3
movw (%A), %D        ; D = RAM[3] (resto)
leaw $2, %A          ; A = 2
movw %D, (%A)        ; RAM[2] = resto

END:
nop