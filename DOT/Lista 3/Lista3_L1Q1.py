'''Lista 1 - Questão 1
Faça uma função que recebe um número inteiro por parâmetro e retorna
verdadeiro se ele for par e falso se for ímpar.'''

def e_par(n):
    if type(n) != int or n <= 0:
        return Exception 
    return n%2 == 0


assert e_par(1) == False
assert e_par(2) == True
assert e_par(0) == Exception
assert e_par(-2) == Exception
assert e_par(2.5) == Exception
assert e_par(" ") == Exception

print("TESTES OK")
