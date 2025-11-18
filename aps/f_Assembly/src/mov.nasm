; Elementos de Sistemas : 2018a
; Rafael Corsi
; Hardware : Z0.1
;
; Data :
;    - Dez 2018
; Descrição :
;    - Movimentação de dados da memoria RAM
;
; RAM[0] = RAM[1]
; RAM[1] = RAM[0] ; (kailyn) entendi q eh p trocar os dois de lugar
; RAM[3] = 1

; temporario
leaw $1, %A       
movw (%A), %D      
leaw $2, %A        
movw %D, (%A)      ; RAM[2] = RAM[1]

leaw $0, %A        
movw (%A), %D      
leaw $1, %A        
movw %D, (%A)      ; RAM[1] = RAM[0]

leaw $2, %A       
movw (%A), %D      ; %D = RAM[2] (valor og de RAM[1])
leaw $0, %A        
movw %D, (%A)    ; RAM[0] = valor antigo de RAM[1]

;RAM[3] = 1
leaw $3, %A        
movw $1, (%A)      ; RAM[3] = 1

END:
leaw $END, %A      
jmp                
nop               
nop                