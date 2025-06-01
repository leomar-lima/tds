'''Lista 1 - Questão 11
Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna
o número de divisores desse valor.'''

def num_divisores(n):
  if type(n) != int or n<=0:
    return Exception
  divisores = 0
  for i in range(1, n + 1):
    if n % i == 0:
      divisores += 1
  return divisores

assert num_divisores(2) == 2
assert num_divisores(4) == 3
assert num_divisores(1) == 1
assert num_divisores(0) == Exception
assert num_divisores(2.0) == Exception
assert num_divisores(-1) == Exception
assert num_divisores(" ") == Exception

print("TESTES OK")