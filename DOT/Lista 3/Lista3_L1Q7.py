'''Lista 1 - Questão 7
Faça um programa para calcular o Fatorial de um número. Para o cálculo do
fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!;
e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é
igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o
número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
número, também do tipo inteiro.'''

def calcular_fatorial(n):
  if type(n) != int or n<0:
    return Exception
  if n == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, n + 1):
      fatorial *= i
    return fatorial

assert calcular_fatorial(5) == 120
assert calcular_fatorial(1) == 1
assert calcular_fatorial(0) == 1
assert calcular_fatorial(-1) == Exception
assert calcular_fatorial(" ") == Exception
assert calcular_fatorial(1.5) == Exception

print("TESTES OK")
