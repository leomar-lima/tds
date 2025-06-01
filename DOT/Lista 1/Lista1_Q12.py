'''Lista 1 - Questão 12
Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e
retorna o somatório desse valor.'''

def somatorio(n):
  soma = 0
  for i in range(1, n + 1):
    soma += i
  return soma

def main():
  while True:
    try:
      numero = int(input("Digite um número inteiro: ").strip())
      if numero < 0:
        print("O número deve ser positivo.")
      else:
        break
    except:
      print("Entrada inválida. Digite um número inteiro.")

  resultado = somatorio(numero)
  print(f"O somatório de {numero} é {resultado}.")


if __name__ == "__main__":
  main()