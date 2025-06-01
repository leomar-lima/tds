'''Questão 7
Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

from random import *

def verificar_pertencimento(lista, valor):
  return valor in lista

def main():
  max_lista = 10
  lista = list(range(max_lista))
  for i in range(max_lista):
    lista[i] = randint(-100, 100)

  print(f"Lista: {lista}")
  valor_procurado = randint(-100, 100)
  print(f"Valor procurado: {valor_procurado}")
  print(f"Pertence à lista: {verificar_pertencimento(lista, valor_procurado)}")

if __name__ == "__main__":
  main()