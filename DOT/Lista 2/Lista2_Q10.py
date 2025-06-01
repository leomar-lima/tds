'''Questão 10
Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

from random import *

def maior_menor(lista):
  maior = lista[0]
  pos_maior = 0
  menor = lista[0]
  pos_menor = 0

  for i in range(1, 15):
      if lista[i] > maior:
          maior = lista[i]
          pos_maior = i
      if lista[i] < menor:
          menor = lista[i]
          pos_menor = i
  return maior, pos_maior, menor, pos_menor


def main():
    lista = []
    for i in range(15):
        lista.append(randint(-100, 100))

    print("Lista: ", lista)

    maior, pos_maior, menor, pos_menor = maior_menor(lista)

    print(f"a) Maior elemento: {maior}, Posição: {pos_maior}")
    print(f"b) Menor elemento: {menor}, Posição: {pos_menor}")

if __name__ == "__main__":
    main()