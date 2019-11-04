# -*- coding: utf-8 -*-
import func
__author__ = "Rebellatto , Kastro"
# "That ain't working,
#  That's the way you do it"


tab1 = func.cria_matrix(40,40)
tab2 = func.cria_matrix(40,40)
tab3 = func.cria_matrix(40,40)

tnavios = {"barco de patrulha":'2',"submarino":'3',"destroyer":'3',"encouraçado":'4',"porta-avião":'5'}
navios = ["barco de patrulha","submarino","destroyer","encouraçado","porta-avião"]


for i in range(5):
    print("jogador 1:")
    func.print_tab(tab1)
    print(navios[i])
    tipo =  tnavios[navios[i]]

    verific = func.verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo)

    func.pos_barco(tab1,verific[0],verific[1], tipo,verific[2])


func.print_tab(tab1)

for i in range(5):

    print("jogador 2:")
    func.print_tab(tab2)
    print(navios[i])

    tipo =  tnavios[navios[i]]
    verific = func.verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo)

    func.pos_barco(tab2,verific[0],verific[1], tipo,verific[2])

func.print_tab(tab2)

while tab1 != tab3 or tab2 != tab3:

    print("jogador 1:")
    func.print_tab(tab1)
    tab2 = func.missil(tab2,x = str(input(" Digite a coluna")), y = str(input("Digite a Fileira:")))
    print('\n')
    print("jogador 2:")
    func.print_tab(tab2)
    tab1 = func.missil(tab1,x = str(input("Digite a coluna")), y = str(input("Digite a Fileira:")))
    print('\n')

if tab1 == tab3:
    print("JOGADOR 2 GANHOU!!!")
else:
    print("JOGADOR 1 GANHOU!!!")
