'''Lista 1 - Questão 5
Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso
ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima). '''

def calcular_peso_ideal(altura, sexo):
  if type(altura) == str or  type(sexo) != int or altura<=0 or (sexo != 1 and sexo !=2) :
    return Exception
  if sexo == 1:
    peso_ideal = (62.1 * altura) - 44.7
  else:
    peso_ideal = (72.7 * altura) - 58
  return peso_ideal

assert round(calcular_peso_ideal(1.65, 2),2) == 61.95
assert round(calcular_peso_ideal(1.65, 1),2) == 57.77
assert calcular_peso_ideal(" ",1) == Exception
assert calcular_peso_ideal(1.65, " ") == Exception
assert calcular_peso_ideal(1.65, 3) == Exception
assert calcular_peso_ideal(1.65, 1.0) == Exception
assert calcular_peso_ideal(-1.65, 1) == Exception
assert calcular_peso_ideal(1.65, -1) == Exception


print("TESTES OK")