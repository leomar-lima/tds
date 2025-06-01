'''Lista 1 - Questão 3
Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma
função chamada celsius para calcular e retornar o valor correspondente em
graus Celsius.
Fórmula: C = ((F-32)/9)*5'''

def celsius(F):
  C = ((F-32)/9)*5
  return C

def main():
  while True:
    try:
      fahrenheit = float(input("Digite uma temperatura em °F: ").strip())
      if fahrenheit < -459.67:
        print("A temperatura não pode ser menor que -459.67°F (Zero Absoluto em Celsius).")
      else:
        break
    except:
      print("Valor inválido. Insira um número.")
  c = celsius(fahrenheit)
  print(f"{fahrenheit}°F equivale a {c:.2f}°C.")

if __name__ == '__main__':
  main()
