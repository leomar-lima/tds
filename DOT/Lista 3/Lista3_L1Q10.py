'''Lista 1 - Questão 10
Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna
o maior. Se forem iguais retorna qualquer um deles;
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida
imprime o maior dos quatro números usando a função Max.'''

def maximo(a , b, c, d):
  maior = a
  for i in (a, b, c, d):
    if i > maior:
      maior = i
  return maior

def encontrar_maior(lista):
  series_maior=[]
  for i in lista:
    if type(i[0]) != int or type(i[1]) != int or type(i[2]) != int or type(i[3]) != int:
      return Exception
    series_maior.append(maximo(i[0],i[1],i[2],i[3]))
  maior = maximo(series_maior[0],series_maior[1],series_maior[2],series_maior[3])
  return series_maior, maior

assert encontrar_maior(((1,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7))) == ([4, 5, 6, 7], 7)
assert encontrar_maior(((-1,2,3,4),(2,3,4,-5),(3,4,5,6),(4,5,-6,-7))) == ([4, 4, 6, 5], 6)
assert encontrar_maior(((1," ",3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7))) == Exception
assert encontrar_maior(((1.0,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7))) == Exception
assert encontrar_maior(((1.0,2,3,4),(2,3,4.0,5),(3,4," ",6),(4,5,6,7))) == Exception
                       
print("TESTES OK")



  
