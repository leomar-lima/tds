'''LISTA 4 - QUESTÃO 2
Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
o número de vezes que cada número ocorre na sequência.
'''


def ocorrencias(lista):
    ocorrencias = {}
    for resultado in lista:
        if type(resultado) != int:
            return Exception
        if resultado in ocorrencias:
            ocorrencias[resultado] += 1
        else:
            ocorrencias[resultado] = 1
    return ocorrencias


assert ocorrencias([1,2,2,2,2,2,2,3,3,4,5,6,6]) == {1: 1, 2: 6, 3: 2, 4: 1, 5: 1, 6: 2}
assert ocorrencias([-1,2,3,3,4,5,6,6]) == {-1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 2}
assert ocorrencias([1,2,2,2,3,3.0,4,5,6]) == Exception
assert ocorrencias([1,2,2,2,2,"a",2,3,3,4,5,6,6]) == Exception

print("TESTES OK!")