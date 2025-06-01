'''Lista 1 - Questão 6
Escreva um programa para ler o número de lados de um polígono regular e a medida
do lado (em cm). Faça um procedimento que receba como parâmetro o número de
lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.'''

def poligono(num_lados, medida_lado):
  if num_lados == 3:
    perimetro = num_lados * medida_lado
    print("TRIÂNGULO")
    print(f"Perímetro: {perimetro:.2f}cm")
  elif num_lados == 4:
    area = medida_lado ** 2
    print("QUADRADO")
    print(f"Área: {area:.2f}cm²")
  elif num_lados == 5:
    print("PENTÁGONO")

def main():
  while True:
    try:
      num_lados = int(input("Digite o número de lados do polígono (3, 4 ou 5): ").strip())
      if num_lados not in [3, 4, 5]:
        print("Número de lados inválido. Digite 3, 4 ou 5.")
      else:
        break
    except:
      print("Valor inválido. Insira um número inteiro.")
  while True:
    try:
      medida_lado = float(input("Digite a medida do lado (em cm): ").strip())
      if medida_lado <= 0:
        print("A medida do lado deve ser maior que zero.")
      else:
        break
    except:
      print("Valor inválido. Insira um número.")
  poligono(num_lados, medida_lado)


if __name__ == "__main__":
  main()