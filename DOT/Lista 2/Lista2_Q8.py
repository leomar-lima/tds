'''Questão 8
Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.'''

from random import *
import string

def count_A(lista):
  count = 0
  for letra in lista:
    if letra == 'A':
      count += 1
  return count

def main():
  lista_letras = [choice(string.ascii_uppercase) for _ in range(10)]
  print(lista_letras)
  print(count_A(lista_letras))

if __name__ == "__main__":
  main()

