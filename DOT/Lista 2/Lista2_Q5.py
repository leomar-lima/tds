'''Questão 5
Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.'''

from random import *

def intercalar_listas(lista1, lista2):
    lista_intercalada = list(range(len(lista1)*2))
    for i in range(len(lista1)):
        lista_intercalada[2 * i] = lista1[i]
        lista_intercalada[2 * i + 1] = lista2[i]
    return lista_intercalada

def main():
  max_lista = 10
  lista1 = list(range(max_lista))
  lista2 = list(range(max_lista))
  for i in range(max_lista):
    lista1[i] = uniform(-100, 100)
    lista2[i] = uniform(-100, 100)
  print(f"Lista 1: {lista1}")
  print(f"Lista 2: {lista2}")
  lista_intercalada = intercalar_listas(lista1, lista2)
  print(f"Lista intercalada: {lista_intercalada}")

if __name__ == "__main__":
  main()
