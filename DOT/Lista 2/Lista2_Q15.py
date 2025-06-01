'''Questão 15
Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
por diante. Escrever todo a lista D e todo a lista E.'''

from random import *

def main():
  D = list(randint(0, 100) for i in range(10))


  E = D[::-1] 

  print(f"Lista D:{D}")
  print(f"Lista E (inversa de D):{E}")

if __name__ == "__main__":
  main()