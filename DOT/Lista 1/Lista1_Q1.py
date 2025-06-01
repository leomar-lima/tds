'''Lista 1 - Questão 1
Faça uma função que recebe um número inteiro por parâmetro e retorna
verdadeiro se ele for par e falso se for ímpar.'''

def e_par(n):
  return n%2 == 0

def main():
  while True:
    try:
      numero = int(input("Digite um número inteiro: ").strip())
      if e_par(numero):
        print(f"O número {numero} é PAR.")
      else:
        print(f"O número {numero} é ÍMPAR.")
      break
    except:
      print("Valor inválido. Insira um número inteiro.")

if __name__ == '__main__':
  main()
