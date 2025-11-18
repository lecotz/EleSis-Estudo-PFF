; Arquivo: Abs.nasm
; Curso: Elementos de Sistemas
; Criado por: Luciano Soares
; Data: 27/03/2017
; Adicione o valor de RAM[1] com RAM[0] gravando em RAM[2].

; D = RAM[0]
leaw $0, %A        
movw (%A), %D      

; D = RAM[0] + RAM[1]
leaw $1, %A        
addw (%A), %D, %D  ; %D = RAM[1] + %D  

; RAM[2] = D
leaw $2, %A        
movw %D, (%A)      ; RAM[2] = soma


END:
leaw $END, %A      
jmp                
nop                