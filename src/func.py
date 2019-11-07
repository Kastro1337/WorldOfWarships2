# -*- coding: utf-8 -*-
__author__ = "Kastro & Rebelatineo"
import random
'''funções para batalha naval.'''

def cria_matrix(vlinha, vcoluna):
    # Cria um tabuleiro mto do bacana
    tabuleiro = []
    for i in range(vlinha):             # cria linhas
        tabuleiro.append(['\u2588']*vcoluna) # cria elementos dentro das linhas, que servem como coluna as well
    return tabuleiro

def print_tab(tabuleiro):
    # Printa esse tabuleiro de maneira razoável
    for i in tabuleiro:# pega um elemento do tabuleiro individualmente.
        print(" ".join(i))

def missil(tab,x,y):
    # manda um teleguiado, very OP
    if tab[int(y)][int(x)] == '\u2588': # se a posição no tabuleiro já for igual a 0 (nulo/água) - (x,y) invertido
        print("Errou")             # mostra erro
        return tab
    else:
        print("Acertou!!!!")       # senão mostra o acerto
        tab[int(y)][int(x)] = '\u2588'  # e substitui a posição
        return  tab


def pos_barco(tab, x, y, tipo, OneDirection='D'):
    # zygmunt barcman. posiciona o barco no tabuleiro
    if  OneDirection.upper() == "D": # posicionado para a direita
        for i in range(int(tipo)):   # O tipo é um número em formato de string
            if tab[y][x + i] != '\u2588':

                for i in range(  int(tipo) ):
                    if tab[y][x+i] == tipo:   tab[y][x+i] = '\u2588'


                print('Opa opa opa você não pode colocar seu barco aqui amigão')
                print('Perdeu um barco')
                break

            else:   tab[y][x+i] = tipo       # as casas posicionadas serão o alcance do tipo para a d






    elif OneDirection.upper() == "B":
        for i in range(int(tipo)):
            if tab[y + i][x] != '\u2588':

                for i in range(  int(tipo) ):
                    if tab[y+i][x] == tipo:   tab[y+i][x] = '\u2588'




                print('Opa opa opa você não pode colocar seu barco aqui amigão')
                print('Perdeu um barco')

                break
            else: tab[y+i][x] = tipo       # as casas posicionadas serão o alcance do tipo para baixo


    return tab





def verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo):

    while True:

        x , y = int(input("Digite a Coluna (x)")) , int(input("Digite a Fileira (y)"))   # pede X e Y e direção dentro da função

        OneDirection = str(input("Digite a direção [D/B]")).upper()






        if OneDirection == 'D' or  OneDirection == 'B'  :


            if not y in range(0,39) or  x not in range(0,39):
                print('Não é um valor válido') 
            else:


                if y + int(tipo) < 40 or  x + int(tipo) < 40 : return (int(x-1),int(y-1),OneDirection) 	
                else: print('Nossos barcos não chegam lá comandante')




        else: print(OneDirection, 'Não e válido como posição') # retorna ao começo do laço, pois não verificou-se posições válidas.

def computador(tipo = 0):
	while True:	
		x = random.randint(0,39)
		y = random.randint(0,39)
		OneDirection = random.choice(['D', 'B'])
		if y + int(tipo) < 40 or  x + int(tipo) < 40 : 
			return (int(x),int(y),OneDirection)
	
