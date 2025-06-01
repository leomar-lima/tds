'''Lista 1 - Questão 7
Faça um programa para calcular o Fatorial de um número. Para o cálculo do
fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!;
e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é
igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o
número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
número, também do tipo inteiro.'''

def calcular_fatorial(n):
  if n == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, n + 1):
      fatorial *= i
    return fatorial

def main():
  while True:
    try:
      numero = int(input("Digite um número inteiro: ").strip())
      if numero < 0:
        print("O número deve ser não negativo.")
      else:
        break
    except:
      print("Entrada inválida. Digite um número inteiro.")
  resultado = calcular_fatorial(numero)
  print(f"O fatorial de {numero} é {resultado}.")


if __name__ == "__main__":
  main()