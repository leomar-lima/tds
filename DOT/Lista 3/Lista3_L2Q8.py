'''Questão 8
Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes
ocorreu a letra ‘A’.'''


def count_A(lista):
  count = 0
  for letra in lista:
    if type(letra) !=str:
      return Exception
    if letra == 'A':
      count += 1
  return count

assert count_A(["A","A","A"]) == 3
assert count_A(["A","B","C","D"]) == 1
assert count_A([1,2,"A"]) == Exception
assert count_A(["A",1.0,"A"]) == Exception
assert count_A(["A",-1.0,"A"]) == Exception

print("TESTES OK")

