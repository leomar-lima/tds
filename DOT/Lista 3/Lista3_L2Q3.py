'''Questão 3
Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''

def inverter_lista(lista):
  lista_inversa = []
  for i in lista:
    if type(i) == str:
      return Exception
    lista_inversa.insert(0,i)

  return lista_inversa

assert inverter_lista([1,2,3,4,5]) == [5,4,3,2,1]
assert inverter_lista([-1,1.0,2,3,4]) == [4,3,2,1.0,-1]
assert inverter_lista(["a",1,2,4]) == Exception

print("TESTES OK")
