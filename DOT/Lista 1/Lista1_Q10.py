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

def verificao_numero_inteiro(posicao):
  while True:
    try:
      numero = int(input(f"Digite o {posicao} número: ").strip())
      return numero
    except:
      print("Entrada inválida. Digite um número inteiro.")

def main():
  lista_maior = []
  for i in range(4):
    a = verificao_numero_inteiro("primeiro")
    b = verificao_numero_inteiro("segundo")
    c = verificao_numero_inteiro("terceiro")
    d = verificao_numero_inteiro("quarto")

    maior_abcd = maximo(a, b, c, d)
    lista_maior.append(maior_abcd)

    print(f"\nSérie {i+1} -> O maior número entre {a}, {b}, {c} e {d} é: {maior_abcd}\n")
  print(f"\nO maior número das Séries é: {maximo(lista_maior[0],lista_maior[1],lista_maior[2],lista_maior[3])}")


if __name__ == "__main__":
  main()