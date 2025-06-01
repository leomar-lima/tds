'''Lista 1 - Questão 14
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!'''


def somatorio_fatorial_invertido(n):
  if type(n) != int or n<=0:
    return Exception
  s = 1
  for i in range(1, n+1):
    fatorial = 1
    for j in range(1, i+1):
      fatorial *= j
    s += 1/fatorial
  return s

assert somatorio_fatorial_invertido(1) == 2
assert round(somatorio_fatorial_invertido(2),2) == 2.50
assert round(somatorio_fatorial_invertido(6),2) == 2.72
assert somatorio_fatorial_invertido(0) == Exception
assert somatorio_fatorial_invertido(-1) == Exception
assert somatorio_fatorial_invertido(1.0) == Exception
assert somatorio_fatorial_invertido(" ") == Exception

print("TESTES OK")