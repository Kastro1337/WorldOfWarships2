# -*- coding: utf-8 -*-
__author__ = "Kastro & Rebelatineo"

'''funções para batalha naval.'''

def cria_matrix(vlinha, vcoluna):
    # Cria um tabuleiro mto do bacana
    tabuleiro = []
    for i in range(vlinha):             # cria linhas
        tabuleiro.append(['0']*vcoluna) # cria elementos dentro das linhas, que servem como coluna as well
    return tabuleiro

def print_tab(tabuleiro):
    # Printa esse tabuleiro de maneira razoável
    for i in tabuleiro:     # pega um elemento do tabuleiro individualmente.
        print(" ".join(i))

def missil(tab,x,y):
    # manda um teleguiado, very OP
    if tab[int(y)][int(x)] == '0': # se a posição no tabuleiro já for igual a 0 (nulo/água) - (x,y) invertido
        print("Errou")             # mostra erro
        return tab
    else:
        print("Acertou!!!!")       # senão mostra o acerto
        tab[int(y)][int(x)] = '0'  # e substitui a posição
        return  tab


def pos_barco(tab, x, y, tipo, OneDirection='D'):
    # zygmunt barcman. posiciona o barco no tabuleiro
    if  OneDirection.upper() == "D": # posicionado para a direita
        for i in range(int(tipo)):   # O tipo é um número em formato de string
            tab[y][x+i] = tipo       # as casas posicionadas serão o alcance do tipo para a direita
    elif OneDirection.upper() == "B":
        for i in range(int(tipo)):
            tab[y+i][x] = tipo       # as casas posicionadas serão o alcance do tipo para baixo
    # else:
    #     raise "Erro, deve ser direção"
    return tab



def verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo):

    while True:
        x = int(input("Digite a Coluna (x)"))     # pede X e Y e direção dentro da função
        y = int(input("Digite a Fileira (y)"))

        OneDirection = str(input("Digite a direção [D/B]")).upper()





        if OneDirection == 'D' or  OneDirection == 'B'  : 	#
            if y in range(1,10) or x in range(1,10):		# TODO: trocar esses 10 por uma váriavel que é o range do tabuleiro
                print('Não é um valor valido')			# por que y e x in range(1,10) são inválidos??????
                break


            if y + int(tipo) < 10 or  x + int(tipo) < 10 :	# se a posição mais o tipo < 10, então é válido e sai do laço while
                break
        print('Valor invalido, Digite novamente \n \n \n ') # retorna ao começo do laço, pois não verificou-se posições válidas.


    return (int(x),int(y),OneDirection) # retorna o x , y e a direção válidos
