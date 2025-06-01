'''Lista 1 - Questão 8
Escreva uma função que lê um caractere digitado pelo usuário e retorna este
caractere somente se ele for igual a 'S' ou 'N'. Se ocaractere não for nem 'S'
nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'.
Use esta função em um programa que fica lendo do usuário um número qualquer e
imprime este número ao cubo na tela. O programa deve ficar lendo os números até
o usuário responder 'N' à pergunta se ele deseja continuar ou não.'''


def ler_caractere():
  while True:
    caractere = input("Deseja continuar (S/N)? ").strip().upper()
    if caractere == 'S' or caractere == 'N':
      return caractere
    else:
      print('Caractere inválido. Digite novamente.')

def main():
  while True:
    try:
      numero = float(input("Digite um número: ").strip())
    except:
      print("Entrada inválida. Digite um número.")
      continue

    cubo = numero ** 3
    print(f"O número {numero} ao cubo é {cubo:.2f}.")

    caractere = ler_caractere()
    if caractere == 'N':
      break

if __name__ == "__main__":
  main()