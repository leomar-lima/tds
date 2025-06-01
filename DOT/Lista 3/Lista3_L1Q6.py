'''Lista 1 - Questão 6
Escreva um programa para ler o número de lados de um polígono regular e a medida
do lado (em cm). Faça um procedimento que receba como parâmetro o número de
lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5.'''

def poligono(num_lados, medida_lado):
  if type(num_lados) != int or num_lados < 3 or num_lados > 5 or type(medida_lado) == str or medida_lado <=0 :
    return Exception
  if num_lados == 3:
    perimetro = num_lados * medida_lado
    return "TRIÂNGULO", perimetro
  elif num_lados == 4:
    area = medida_lado ** 2
    return "QUADRADO", area
  elif num_lados == 5:
    return "PENTÁGONO", None

assert poligono(3,2) == ("TRIÂNGULO", 6)
assert poligono(4,2) == ("QUADRADO", 4)
assert poligono(5,5) == ("PENTÁGONO", None)
assert poligono(3, 1.5) == ("TRIÂNGULO", 4.5)
assert poligono(3, " ") == Exception
assert poligono(1,2) == Exception
assert poligono (4.0, 2) == Exception
assert poligono (" ", 1) == Exception
assert poligono (3, -2) == Exception
assert poligono (3, 0) == Exception
assert poligono (-2, 2) == Exception

print("TESTES OK")

