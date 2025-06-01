'''Questão 14
Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.'''
from random import *

def main():
  c = list(randint(-100, 100) for i in range(10))
  print("Lista C:", c)

  for i in range(len(c)):
    if c[i] < 0:
      c[i] = 0

  print(f"Lista C modificada: {c}")

if __name__ == "__main__":
  main()