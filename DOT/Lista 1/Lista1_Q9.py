'''Lista 1 - Questão 9
Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna
a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta
função em um programa que lê n1 e n2 do usuário e imprime a soma.'''

def soma_intervalo(n1, n2):
  soma = 0
  for i in range(n1, n2 + 1):
    soma += i
  return soma

def main():
  while True:
    try:
      numero1 = int(input("Digite o primeiro número inteiro: ").strip())
      break
    except:
      print("Entrada inválida. Digite um número inteiro.")
  while True:
    try:
      numero2 = int(input("Digite o segundo número inteiro: ").strip())
      if numero2 < numero1:
        print("O segundo número deve ser maior ou igual ao primeiro.")
        continue
      break
    except:
      print("Entrada inválida. Digite um número inteiro.")

  soma = soma_intervalo(numero1, numero2)
  print(f"A soma dos números inteiros no intervalo [{numero1}, {numero2}] é: {soma}")

if __name__ == "__main__":
  main()