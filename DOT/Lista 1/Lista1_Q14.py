'''Lista 1 - Questão 14
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/1! + 1⁄2! + 1/3! + 1 /N!'''


def somatorio_fatorial_invertido(n):
  s = 1
  for i in range(1, n+1):
    fatorial = 1
    for j in range(1, i+1):
      fatorial *= j
    s += 1/fatorial
  return s

def main():
  while True:
    try:
      numero = int(input("Digite um número inteiro positivo: ").strip())
      if numero <= 0:
        print("O número deve ser positivo.")
      else:
        break
    except:
      print("Entrada inválida. Digite um número inteiro.")
  print(f"O somatório invertido do fatorial de {numero} é {somatorio_fatorial_invertido(numero):.2f}.")

if __name__ == "__main__":
  main()