'''Questão 1
Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista.'''

from random import *

def main():
  max_lista = 100
  lista = list(range(max_lista))
  quant_pares=0
  quant_impares=0
  lista_pares=[]
  lista_impares=[]

  for i in range(max_lista):
    lista[i] = randint(-100,100)
    if(lista[i]%2==0):
      lista_pares.append(lista[i])
      quant_pares +=1
    else:
      lista_impares.append(lista[i])
      quant_impares +=1
  print(f"Lista: {lista}")
  print(f"A) Quantidade de números pares: {quant_pares}")
  print(f"B) Lista de números pares: {lista_pares}")
  print(f"C) Quantidade de números ímpares: {quant_impares}")
  print(f"D) Lista de números ímpares: {lista_impares}")

if __name__ == "__main__":
  main()