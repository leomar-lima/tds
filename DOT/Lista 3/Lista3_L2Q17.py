'''Questão 17
Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o
valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V
aparece.
Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto.'''

def buscar(W:list,V):
  ocorrencias = []
  count = 0
  for i in range(len(W)):
    if type(W[i]) == str or len(W)!=10:
       return Exception
    if W[i] == V:
      count += 1
      ocorrencias.append(i)
  if count > 0:
      return count, ocorrencias
  else:
     return None

assert buscar([1,2,3,4,5,6,7,8,9,10],5) ==(1, [4])
assert buscar([-1,2,3,3,4,5,6,7,8,9],3) == (2, [2,3])
assert buscar([1,2,3,4.0,4,5,6,7,8,4],4) == (3, [3,4,9])
assert buscar([1,2,3,4.0,4,5,6,7,8,4],9) == None
assert buscar([1,2,3," ",4,5,6,7,8,4],4) == Exception
assert buscar([1,2,3,4,5,6,7,8,4],4) == Exception

print("TESTES OK")