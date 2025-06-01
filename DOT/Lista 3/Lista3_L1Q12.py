'''Lista 1 - Questão 12
Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.'''

def somatorio(n):
  if type(n) != int or n<0:
    return Exception
  soma = 0
  for i in range(1, n + 1):
    soma += i
  return soma

assert somatorio(1) == 1
assert somatorio(5) == 15
assert somatorio(0) == 0
assert somatorio(-1) == Exception
assert somatorio(" ") == Exception
assert somatorio(1.0) == Exception

print("TESTES OK")
