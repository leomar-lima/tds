'''Questão 9
Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.'''

def inverter_lista(lista):
  lista_inversa = lista[::-1]
  return lista_inversa

def main():
  lista = []
  for i in range(5):
    while True:
      try:
        n = int(input(f"Digite o {i+1}º número inteiro: "))
        lista.append(n)
        break
      except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

  print(f"Lista X: {lista}")
  lista_inversa = inverter_lista(lista)
  print(f"Lista Y (inversa): {lista_inversa}")

if __name__ == "__main__":
  main()

