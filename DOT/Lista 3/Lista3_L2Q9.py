'''Questão 9
Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.'''

def inverter_lista(lista):
  lista_inversa = []
  for i in lista:
    if type(i) == str or len(lista)!=5:
      return Exception
    lista_inversa.insert(0,i)

  return lista_inversa

assert inverter_lista([1,2,3,4,5]) == [5,4,3,2,1]
assert inverter_lista([-1,1.0,2,3,4]) == [4,3,2,1.0,-1]
assert inverter_lista(["a",1,2,3,4]) == Exception

print("TESTES OK")
