'''Questão 14
Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
Escrever a lista C modificada.'''

def modificar_negativo(c):
  for i in range(len(c)):
    if type(c[i]) != int:
      return Exception
    if c[i] < 0:
      c[i] = 0

  return c

assert modificar_negativo([-1,1,2,3,-4,5]) == [0,1,2,3,0,5]
assert modificar_negativo(["A",1,2,-3]) == Exception
assert modificar_negativo([1.0,-1.0]) == Exception

print("TESTES OK")