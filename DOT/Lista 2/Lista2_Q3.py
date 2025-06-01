'''Questão 3
Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''

def inverter_lista(lista):
  lista_inversa = lista[::-1]
  return lista_inversa

def main():
  lista = []
  while True:
    try:
      n = float(input("Digite um número (ou algo diferente para parar): "))
    except:
      break
    lista.append(n)
  print(f"Lista: {lista}")
  lista_inversa = inverter_lista(lista)
  print(f"Lista inversa: {lista_inversa}")

if __name__ == "__main__":
  main()