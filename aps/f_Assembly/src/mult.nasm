; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017

; Multiplica o valor de RAM[1] com RAM[0] salvando em RAM[3]


Loop:
leaw $0, %A         
movw (%A), %D       
leaw $FIM, %A       
je
nop

leaw $1, %A         
movw (%A), %D       
leaw $3, %A        
addw (%A), %D, (%A) 

leaw $0, %A        
movw (%A), %D
decw %D
movw %D, (%A)

leaw $Loop, %A     
jmp
nop

FIM:
nop                 
