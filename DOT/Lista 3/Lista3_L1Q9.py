'''Lista 1 - Questão 9
Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna
a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta
função em um programa que lê n1 e n2 do usuário e imprime a soma.'''

def soma_intervalo(n1, n2):
  if type(n1) != int or type(n2) != int or n2<n1:
    return Exception
  soma = 0
  for i in range(n1, n2 + 1):
    soma += i
  return soma

assert soma_intervalo(1,5) == 15
assert soma_intervalo(-1,3) == 5
assert soma_intervalo(0, 0) == 0
assert soma_intervalo(" ",1) == Exception
assert soma_intervalo(3, 2) == Exception
assert soma_intervalo(2, " ") == Exception
assert soma_intervalo(2.1, 5) == Exception
assert soma_intervalo(2, 5.0) == Exception

print("TESTES OK")
