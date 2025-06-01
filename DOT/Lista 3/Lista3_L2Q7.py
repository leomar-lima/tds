'''Questão 7
Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
outro valor dado pertence ou não à lista.'''

from random import *

def verificar_pertencimento(lista, valor):
  for i in lista:
    if type(i) == str or len(lista) !=10:
      return Exception
  return valor in lista

assert verificar_pertencimento([1,2,3,4,4,6,7,8,9,10],5) == False
assert verificar_pertencimento([1,2,3,-4,5.0,6,7,8,9,10],5) == True
assert verificar_pertencimento([1,2,3,4],5) == Exception
assert verificar_pertencimento([1,2,3," ",5,6,7,8,9,10],5) == Exception


print("TESTES OK")
