'''Lista 1 - Questão 3
Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma
função chamada celsius para calcular e retornar o valor correspondente em
graus Celsius.
Fórmula: C = ((F-32)/9)*5'''

def para_celsius(F):
  if type(F) == str or F < -459.67:
       return Exception
  C = ((F-32)/9)*5
  return C

assert para_celsius(32) == 0
assert round(para_celsius(-459.67),2) == -273.15
assert para_celsius(-460) == Exception
assert para_celsius(" ") == Exception

print("TESTES OK")
