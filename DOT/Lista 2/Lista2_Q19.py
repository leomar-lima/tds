'''Questão 19
Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.
'''

from random import *

def main():
  R = list(randint(0, 100) for i in range(5))
  S = list(randint(0, 100) for i in range(10))
  X = R + S[:5]

  print(f"Lista X: {X}")

if __name__ == "__main__":
  main()