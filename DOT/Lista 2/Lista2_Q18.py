'''Questão 18
Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
'''

from random import *

def main():
  X = list(randint(-100, 100) for i in range(10))
  R = []
  for i in range(len(X)):
    if X[i] < 0:
      R.append(X[i])


  print(f"Lista X: {X}")
  print(f"Lista R: {R}")

if __name__ == "__main__":
  main()