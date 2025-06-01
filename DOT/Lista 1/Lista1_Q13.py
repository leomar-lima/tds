'''Lista 1 - Questão 13
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1⁄2 + 1/3 + 1⁄4 + 1/5 + 1/N.'''

def somatorio_invertido(n):
  s = 0
  for i in range(1,n+1):
    s += 1/i
  return s

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

  print(f"O somatório invertido de {numero} é {somatorio_invertido(numero):.2f}.")

if __name__ == "__main__":
  main()