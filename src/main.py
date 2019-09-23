# -*- coding: utf-8 -*-
import func
__author__ = "Kastro"
# "That ain't working,
#  That's the way you do it"

tab1 = func.cria_matrix(10,10)
tab2 = func.cria_matrix(10,10)

# Note: tab1[y][x]
tab1 = func.pos_barco(tab1,0,0,'3','D')
#tab1[0][0] = 'X'

func.print_tab(tab1)
tab1 = func.missil(tab1,0,0)
print("teste")
func.print_tab(tab1)

#TODO: HIT or MISS aviso
#TODO: lógica de jogo aplicada

'''
backuptab1 = tab1
# Não funciona pq listas tem vida própria
if backuptab1 == tab1:
    print("miss")
else:
    print('hit')
'''
