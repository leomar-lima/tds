'''Lista 1 - Questão 13
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.'''

def somatorio_invertido(n):
  if type(n) != int or n<=0:
    return Exception
  s = 0
  for i in range(1,n+1):
    s += 1/i
  return s

assert somatorio_invertido(1) == 1
assert somatorio_invertido(2) == 1.5
assert round(somatorio_invertido(6),2) == 2.45
assert somatorio_invertido(0) == Exception
assert somatorio_invertido(-1) == Exception
assert somatorio_invertido(1.0) == Exception
assert somatorio_invertido(" ") == Exception

print("TESTES OK")

