'''Questão 16
Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.'''

from random import *

def main():
  X = list(randint(0, 100) for i in range(10))
  Y = []
  for i in range(len(X)):
    if i % 2 == 0:
      Y.append(X[i] / 2)
    else:
      Y.append(X[i] * 3)
  print(f"Lista X: {X}")
  print(f"Lista Y: {Y}")

if __name__ == "__main__":
  main()