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
    for i in tabuleiro:# pega um elemento do tabuleiro individualmente.
        for j in range(len(i)):
            if i[j] == '0':
                i[j] = '\u2588'
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
            if tab[y][x + i] != '0':

                for i in range(  int(tipo) ):
                    if tab[y][x+i] == tipo:   tab[y][x+i] = '0'


                print('Opha opa opa você não pode colocar seu barco aqui amigão')
                print('Pedeu um barco OTARIO')
                break

            else:   tab[y][x+i] = tipo       # as casas posicionadas serão o alcance do tipo para a d






    elif OneDirection.upper() == "B":
        for i in range(int(tipo)):
            if tab[y + i][x] != '0':

                for i in range(  int(tipo) ):
                    if tab[y+i][x] == tipo:   tab[y+i][x] = '0'




                print('Opha opa opa você não pode colocar seu barco aqui amigão')
                print('Pedeu um barco OTARIO')

                break
            else: tab[y+i][x] = tipo       # as casas posicionadas serão o alcance do tipo para baixo


    return tab





def verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo):

    while True:

        x , y = int(input("Digite a Coluna (x)")) , int(input("Digite a Fileira (y)"))   # pede X e Y e direção dentro da função

        OneDirection = str(input("Digite a direção [D/B]")).upper()






        if OneDirection == 'D' or  OneDirection == 'B'  :


            if not y in range(0,10) or  x not in range(0,10):
                print('Não é um valor valido') 
            else:


                if y + int(tipo) < 10 or  x + int(tipo) < 10 : return (int(x),int(y),OneDirection) 	
                else: print('Nossos barcos não chegam lá comandante')




        else: print(OneDirection, 'Não e valido como posição') # retorna ao começo do laço, pois não verificou-se posições válidas.


