'''Questão 5
Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.'''

from random import *

def intercalar_listas(lista1, lista2):
    lista_intercalada = list(range(len(lista1)*2))
    for i in range(len(lista1)):
        if type(lista1[i]) == str or type(lista2[i]) == str or len(lista1) != 5 or len(lista2) != 5:
            return Exception
        lista_intercalada[2 * i] = lista1[i]
        lista_intercalada[2 * i + 1] = lista2[i]
    return lista_intercalada

assert intercalar_listas([1,2,3,4.0,5],[-1,-2,-3,-4,-5]) == [1, -1, 2, -2, 3, -3, 4.0, -4, 5, -5]
assert intercalar_listas(["a","b","c","d","e"],[1,2,3,4,5]) == Exception
 
print("TESTES OK")