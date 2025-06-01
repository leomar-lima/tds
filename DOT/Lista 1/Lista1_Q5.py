'''Lista 1 - Questão 5
Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso
ideal que receba a altura e o sexo via parâmetro e
que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) – 58
- para mulheres : (62.1 * h) – 44.7
Observação: Altura = h (na fórmula acima). '''

def calcular_peso_ideal(altura, sexo):
  if sexo == 1:
    peso_ideal = (62.1 * altura) - 44.7
  else:
    peso_ideal = (72.7 * altura) - 58
  return peso_ideal

def main():
  while True:
    try:
      altura = float(input("Digite a altura, em metros: ").strip())
      if altura < 0:
        print("A altura não pode ser negativa.")
      else:
        break
    except:
      print("Valor inválido. Insira um número.")

  while True:
    try:
      sexo = int(input("Digite o sexo (1 para feminino e 2 para masculino): ").strip())
      if sexo != 1 and sexo != 2:
        print("O sexo deve ser 1 para feminino ou 2 para masculino.")
      else:
        break
    except:
      print("Valor inválido. Insira um número.")

  peso_ideal = calcular_peso_ideal(altura, sexo)
  print(f"O peso ideal para uma pessoa com altura {altura}m e sexo {'femenino' if sexo == 1 else 'masculino'} é {peso_ideal:.2f}kg.")

if __name__ == '__main__':
  main()