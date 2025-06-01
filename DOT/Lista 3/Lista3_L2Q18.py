'''Questão 18
Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
'''

from random import *

def lista_R(X):
  R = []
  for i in range(len(X)):
    if type(X[i]) == str or len(X)!=10:
      return Exception
    if X[i] < 0:
      R.append(X[i])
  return R

assert lista_R([1,-2,3,-4,5,-6.0,7,-8,9,-10.0]) == [-2,-4,-6,-8,-10]
assert lista_R([1,2,3, 4,5,6,7,8,9,10]) == []
assert lista_R([" ",2,3, 4,5,6,7,8,9,10]) == Exception
assert lista_R([2,3, 4,5,6,7,8,9,10]) == Exception

print("TESTES OK")