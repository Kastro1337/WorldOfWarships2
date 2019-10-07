# -*- coding: utf-8 -*-
__author__ = "Kastro & Rebelatineo"


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
    if tab[int(y)][int(x)] == '0':
        print("Errou")
        return tab
    else:
        print("Acertou!!!!")
        tab[int(y)][int(x)] = '0'
        return  tab


def pos_barco(tab, x, y, tipo, OneDirection='R'):
    # zygmunt barcman
    if  OneDirection.upper() == "R":
        for i in range(int(tipo)):
            tab[y][x+i] = tipo
    elif OneDirection.upper() == "D":
        for i in range(int(tipo)):
            tab[y+i][x] = tipo 
    else:
        raise "Erro, deve ser direção"
    return tab



def verifica_se_a_posicao_que_o_usuario_escolheu_eh_valida(tipo):
    
    while True:
        x = int(input("Digite a Coluna (x)"))
        y = int(input("Digite a Fileira (y)"))

        OneDirection = str(input("Digite a direção [R/D]")).upper()
        
        
        
        
        
     #   print('aquii')
        
        if OneDirection == 'R' or  OneDirection == 'D'  :
         #   print('Caiu aquiii')
            if y + int(tipo) < 10 or  x + int(tipo) < 10 :
                
          #      print('Caiu aqui')
                break
        print('Valor invalido, Digite novamente \n \n \n ')
                

    return (x,y,OneDirection)
    
