# -*- coding: utf-8 -*-
import func
__author__ = "Kastro"
# "That ain't working,
#  That's the way you do it"

tamanho_tab = 10
 
tab1 = func.cria_matrix(tamanho_tab,tamanho_tab)
tab2 = func.cria_matrix(tamanho_tab,tamanho_tab)
tab3 = func.cria_matrix(tamanho_tab,tamanho_tab)



for i in range(5):
    print("jogador 1:")
    func.print_tab(tab1)
    print(i)
    tipo = str(i+1)
    
    verific = func.verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo)
    
    func.pos_barco(tab1,verific[0],verific[1], tipo,verific[2])



for i in range(5):

    print("jogador 2:")
    func.print_tab(tab2)
    print(i)
    tipo = str(i+1)
    verific = func.verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo)
    
    func.pos_barco(tab2,verific[0],verific[1], tipo,verific[2])


while tab1 != tab3 or tab2 != tab3:

    print("jogador 1:")
    print(func.print_tab(tab1))
    print('\n')
    print("jogador 2:")
    print(func.print_tab(tab2))

# TODO: aplicar lógica de jogo
# TODO: printar Acertou / errou
# TODO: posicionar o número de casas do barco, dicionario
# TODO: bota teu nome de junto do __author__
