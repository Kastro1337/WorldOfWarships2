'''class naval:
    def __init__(self):
        pass
    def __main__(self):
        pass
    # Manzurri, nsei usar class, favor perdoar
'''


 # Cria um tabuleiro mto do bacana
def tabuleiro1(vlinha = 40, vcoluna = 40):
    matriz = []
    linha = []
    for i in range(vcoluna):
        linha.append(" ")
    for i in range(vlinha):
        matriz.append(linha)
    return matriz
