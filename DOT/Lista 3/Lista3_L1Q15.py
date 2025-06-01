'''Lista 1 - Questão 15
Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)'''

def somatorio_formula(t):
  if type(t) != int or t<=0:
    return Exception
  s = 0
  for i in range(1, t+1):
    s += (i**2 + 1)/(i+3)
  return s

assert round(somatorio_formula(1),2) == 0.50
assert round(somatorio_formula(2),2) == 1.50
assert round(somatorio_formula(6),2) == 12.96
assert somatorio_formula(0) == Exception
assert somatorio_formula(-1) == Exception
assert somatorio_formula(1.0) == Exception
assert somatorio_formula(" ") == Exception

print("TESTES OK")
