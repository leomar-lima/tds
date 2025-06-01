'''Questão 16
Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.'''

from random import *

def lista_Y(X):
  Y = []
  for i in range(len(X)):
    if type(X[i]) != int or X[i]<=0 or len(X) != 10:
      return Exception
    if i % 2 == 0:
      Y.append(X[i] / 2)
    else:
      Y.append(X[i] * 3)
  return Y

assert lista_Y([1,2,3,4,5,6,7,8,9,10]) == [0.5, 6, 1.5, 12, 2.5, 18, 3.5, 24, 4.5, 30]
assert lista_Y([-1,2,3,4,5,6,7,8,9,10]) == Exception
assert lista_Y([1.0,2,3,4,5,6,7,8,9,10]) == Exception
assert lista_Y([" ",2,3,4,5,6,7,8,9,10]) == Exception
assert lista_Y([0,2,3,4,5,6,7,8,9,10]) == Exception
assert lista_Y([-1,1,2,3,4,5,6,7,8,9,10]) == Exception
assert lista_Y([2,3,4,5,6,7,8,9,10]) == Exception

print("TESTES OK")