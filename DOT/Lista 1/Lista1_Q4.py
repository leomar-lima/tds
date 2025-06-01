'''Lista 1 - Questão 4
Escreva um programa para ler as notas das duas avaliações de um aluno no
semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem
“PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação). '''

def calcular_media(n1, n2):
  media = (n1 + n2) / 2
  return media

def main():
  while True:
    try:
      nota1 = float(input("Digite a primeira nota: ").strip())
      if nota1 < 0 or nota1 > 10:
        print("A nota não pode ser menor que 0 ou maior que 10.")
      else:
        break
    except:
      print("Valor inválido. Insira um número.")
  while True:
    try:
      nota2 = float(input("Digite a segunda nota: ").strip())
      if nota2 < 0 or nota2 > 10:
        print("A nota não pode ser menor que 0 ou maior que 10.")
      else:
        break
    except:
      print("Valor inválido. Insira um número.")
  media = calcular_media(nota1, nota2)
  print(f"A média é {media:.2f}.")
  if media >= 6:
    print("PARABÉNS! Você foi aprovado!")

if __name__ == '__main__':
  main()