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


def pos_barco(tab, x, y, tipo, OneDirection='D'):
    # zygmunt barcman. posiciona o barco no tabuleiro
    if  OneDirection.upper() == "D": # posicionado para a direita
        for i in range(int(tipo)):   # O tipo é um número em formato de string
            if tab[y][x + i] != '\u2588':
                for i in range( int(tipo) ):
                    if tab[y][x+i] == tipo:
                        tab[y][x+i] = '\u2588'
      
                print('Opha opa opa você não pode colocar seu barco aqui amigão')
                print('Pedeu um barco OTARIO')
                break
            else:
                tab[y][x+i] = tipo       # as casas posicionadas serão o alcance do tipo para a d    
    elif OneDirection.upper() == "B":
        for i in range(int(tipo)):
            if tab[y+i][x] != '\u2588':
                for i in range(int(tipo)):
                    if tab[y+i][x] == tipo:   tab[y+i][x] = '\u2588'

                print('Opha opa opa você não pode colocar seu barco aqui amigão')
                print('Pedeu um barco OTARIO')

                break
            else:
                tab[y+i][x] = tipo       # as casas posicionadas serão o alcance do tipo para baixo
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
    
