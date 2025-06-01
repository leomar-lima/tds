'''Questão 1
Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista.'''


def lista_par_impar(lista):
  quant_pares=0
  quant_impares=0
  lista_pares=[]
  lista_impares=[]

  for i in lista:
    if type(i) != int:
        return Exception
    if(i%2==0):
      lista_pares.append(i)
      quant_pares +=1
    else:
      lista_impares.append(i)
      quant_impares +=1

  return lista_pares, quant_pares, lista_impares, quant_impares

assert lista_par_impar([1,2,3,4,5]) == ([2,4],2,[1,3,5],3)
assert lista_par_impar([1,-2,3,4,5,6,-7,8,9,10]) == ([-2,4,6,8,10],5,[1,3,5,-7,9],5)
assert lista_par_impar([1.0,1]) == Exception
assert lista_par_impar(["1"," "]) == Exception

print("TESTES OK")