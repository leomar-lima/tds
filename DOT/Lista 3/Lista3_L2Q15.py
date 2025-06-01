'''Questão 15
Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''


def inversa(D):
  if len(D)!=10:
    return Exception
  E = D[::-1] 
  return E


assert inversa([1,2,3,4,5,6,7,8,9,10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert inversa(["A","B","C","D","E","F","G","H","I","J"]) == ["J","I","H","G","F","E","D","C","B","A"]
assert inversa([1,2,3]) == Exception
assert inversa(["A","B","C"]) == Exception

print("TESTES OK")