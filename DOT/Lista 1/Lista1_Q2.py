'''Lista 1 - Questão 2
Escreva um programa que leia o raio de um círculo e faça duas funções: uma
função chamada área que calcula e retorna a área do círculo e outra função
chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r;'''

import math

def calcular_area(r):
  area = math.pi * r ** 2
  return area

def calcular_perimetro(r):
  perimetro = 2 * math.pi * r
  return perimetro

def main():
  while True:
    try:
      raio = float(input("Digite um raio de um círculo: ").strip())
      if raio <= 0:
        print("A medida do raio deve ser maior que zero.")
      else:
        break
    except:
      print("Valor inválido. Insira um número positivo.")
  area = calcular_area(raio)
  perimetro = calcular_perimetro(raio)
  print(f"O círculo de raio {raio} u.m tem área de {area:.2f} u.m e perímetro de {perimetro:.2f} u.m.")
  print("* u.m = unidade de medida")


if __name__ == '__main__':
  main()