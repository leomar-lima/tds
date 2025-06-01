'''Lista 1 - Questão 2
Escreva um programa que leia o raio de um círculo e faça duas funções: uma
função chamada área que calcula e retorna a área do círculo e outra função
chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r;'''

import math

def calcular_area(r):
    if type(r) == str or r <= 0:
       return Exception
    area = math.pi * r ** 2
    return area

def calcular_perimetro(r):
  if type(r) == str or r <= 0:
       return Exception
  perimetro = 2 * math.pi * r
  return perimetro

assert round(calcular_area(1),2) == 3.14
assert round(calcular_area(2),2) == 12.57
assert round(calcular_area(2.5),2) == 19.63
assert calcular_area(0) == Exception
assert calcular_area(-1) == Exception
assert calcular_area(" ") == Exception
assert round(calcular_perimetro(1),2) == 6.28
assert round(calcular_perimetro(2),2) == 12.57
assert round(calcular_perimetro(2.5),2) == 15.71
assert calcular_perimetro(0) == Exception
assert calcular_perimetro(-1) == Exception
assert calcular_perimetro(" ") == Exception

print("TESTES OK")


