'''Questão 4
Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''


def maior_menor(lista):
  maior = lista[0]
  pos_maior = 0
  menor = lista[0]
  pos_menor = 0

  for i in range(len(lista)):
      if type(lista[i]) == str:
          return Exception
      if lista[i] > maior:
          maior = lista[i]
          pos_maior = i
      if lista[i] < menor:
          menor = lista[i]
          pos_menor = i
  return maior, pos_maior, menor, pos_menor


assert maior_menor([1,2,3,4,5]) == (5,4,1,0)
assert maior_menor([3,5.0,-1,4,2]) == (5.0,1,-1,2)
assert maior_menor(["a",1,2]) == Exception

print("TESTES OK")

