# -*- coding: utf-8 -*-
import func
__author__ = "Kastro"
# "That ain't working,
#  That's the way you do it"

tab1 = func.cria_matrix(10,10)
tab2 = func.cria_matrix(10,10)
tab3 = func.cria_matrix(10,10)


for i in range(5):
    print("jogador 1:")
    func.print_tab(tab1)
    print(i)
    func.pos_barco(tab1,x = int(input("Digite a Coluna")),y = int(input("Digite a Fileira")), tipo = str(i+1),OneDirection = input("Digite a direção [R/D]"))

for i in range(5):

    print("jogador 2:")
    func.print_tab(tab2)
    print(i)
    func.pos_barco(tab2,x = int(input("Digite a Coluna")),y = int(input("Digite a Fileira")), tipo = str(i+1),OneDirection = input("Digite a direção [R/D]"))


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
