'''Questão 19
Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
de S. Escrever a lista X.
'''

def lista_X(R,S):
  if len(R)!=5 or len(S)!=10:
    return Exception
  X = R + S

  return X

assert lista_X([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10]) == [1,2,3,4,5,1,2,3,4,5,6,7,8,9,10]
assert lista_X(["A",2,3,4,5],[1.0,2,3,4,5,6,7,8,9,"B"]) == ["A",2,3,4,5,1.0,2,3,4,5,6,7,8,9,"B"]
assert lista_X(["A"],[1.0,2,3,4,5,6,7,8,9,"B"]) == Exception
assert lista_X(["A","B",3,4,5],[2,3,4,5,6,7,8,9,"B"]) == Exception

print("TESTES OK")

