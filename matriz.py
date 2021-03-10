from random import randint

entradas = []

def gerar(tamanho):
    for i in range(tamanho):
        entradas.append(randint(0, 100))
    
    return entradas



    
    