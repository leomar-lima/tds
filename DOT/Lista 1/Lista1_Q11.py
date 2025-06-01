'''Lista 1 - Questão 11
Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna
o número de divisores desse valor.'''

def num_divisores(n):
  divisores = 0
  for i in range(1, n + 1):
    if n % i == 0:
      divisores += 1
  return divisores

def main():
  while True:
    try:
      numero = int(input("Digite um número inteiro: ").strip())
      if numero <= 0:
        print("O número deve ser positivo.")
      else:
        break
    except:
      print("Entrada inválida. Digite um número inteiro.")
  divisores = num_divisores(numero)
  print(f"O número {numero} tem {divisores} divisores.")

if __name__ == "__main__":
  main()