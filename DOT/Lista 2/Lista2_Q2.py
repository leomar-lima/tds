'''Questão 2
Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''

from random import *
def main():
  max_lista = 10
  lista = list(range(max_lista))
  quant_negativos = 0
  soma_positivos = 0

  for i in range(max_lista):
    lista[i] = uniform(-100, 100)
    if lista[i] < 0:
      quant_negativos += 1
    else:
      soma_positivos += lista[i]

  print(f"Lista: {lista}")
  print(f"Quantidade de números negativos: {quant_negativos}")
  print(f"Soma dos números positivos: {soma_positivos}")

if __name__ == "__main__":
  main()