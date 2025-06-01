'''Questão 13 Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de
cada face.'''



def ocorrencias_faces(resultados):
    ocorrencias = {}
    for resultado in resultados:
        if type(resultado) != int or resultado<=0 or resultado>6:
            return Exception
        if resultado in ocorrencias:
            ocorrencias[resultado] += 1
        else:
            ocorrencias[resultado] = 1
    return ocorrencias


assert ocorrencias_faces([1,2,2,2,2,2,2,3,3,4,5,6,6]) == {1: 1, 2: 6, 3: 2, 4: 1, 5: 1, 6: 2}
assert ocorrencias_faces([-1,2,3,3,4,5,6,6]) == Exception
assert ocorrencias_faces([1,2,2,2,3,3.0,4,5,6]) == Exception
assert ocorrencias_faces([1,2,2,2,2,"a",2,3,3,4,5,6,6]) == Exception

print("TESTES OK")