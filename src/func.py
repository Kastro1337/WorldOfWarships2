# -*- coding: utf-8 -*-
__author__ = "Kastro"


'''def cria_matrix(vlinha = 40, vcoluna = 40):
    matriz = []
    linha = []
    for i in range(vcoluna):
        linha.append("0")
    for i in range(vlinha):
        matriz.append(linha)
    return matriz

'''
def cria_matrix(vlinha, vcoluna):
    # Cria um tabuleiro mto do bacana
    tabuleiro = []
    for i in range(vlinha):
        tabuleiro.append(['0']*vcoluna)
    return tabuleiro

def print_tab(tabuleiro):
    # Printa esse tabuleiro de maneira razoável
    for i in tabuleiro:
        print(" ".join(i))

def missil(tab,x,y):
    # manda um teleguiado, very OP
    if tab[y][x] == '0':
        return tab
    else:
        tab[y][x] = '0'
        return  tab 

def pos_barco(tab, x, y, tipo, OneDirection='R'): 
    # zygmunt barcman
    if  OneDirection.upper() == "R":
        tab[y][x] = tipo
    elif OneDirection.upper() == "D":
        tab[y][x] = tipo
    else:
        raise "Erro, deve ser direção"
    return tab
