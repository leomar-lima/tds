'''Lista 1 - Questão 15
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)'''

def somatorio_formula(t):
  s = 0
  for i in range(1, t+1):
    s += (i**2 + 1)/(i+3)
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
  print(f"O somatório da fórmula (t^2+1)/(t+3) com t = {numero} é {somatorio_formula(numero):.2f}.")

if __name__ == "__main__":
  main()