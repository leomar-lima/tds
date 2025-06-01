'''Questão 17
Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.
Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.'''

from random import *

def main():
  W = list(randint(0, 100) for i in range(10))
  print("Lista W:", W)
  V = randint(0, 100)
  print("Valor V:", V)
  ocorrencias = []
  count = 0
  for i in range(len(W)):
    if W[i] == V:
      count += 1
      ocorrencias.append(i)
  

  if count > 0:
      print(f"O valor {V} ocorre {count} vezes na lista W.")
      print(f"Posições: {ocorrencias}")
  else:
      print(f"O valor {V} não ocorre nenhuma vez na lista W.")

if __name__ == "__main__":
  main()