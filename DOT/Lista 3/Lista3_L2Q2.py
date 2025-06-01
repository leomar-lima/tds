'''Questão 2
Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''
def lista_num_reais(lista):
  quant_negativos = 0
  soma_positivos = 0

  for i in lista:
    if type(i) != int or len(lista)!=10:
      return Exception
    if i < 0:
      quant_negativos += 1
    else:
      soma_positivos += i
  return quant_negativos, soma_positivos
  

assert lista_num_reais([-1,2,-3,4,-5,6,-7,8,-9,10]) == (5,30)
assert lista_num_reais([-1,2]) == Exception
assert lista_num_reais([-1.0,2,-3,4,-5,6,-7,8,-9,10]) == Exception
assert lista_num_reais([-1,2,-3,4,-5,6,-7,8,-9," "]) == Exception

print("TESTES OK")

