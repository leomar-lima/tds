import csv

def cidades(lista):
    cidades = []
    for i in lista:
        if i[2] not in cidades:
            cidades.append(i[2])
    return cidades


def pessoas_cidades(lista, cidade):
    pessoas = []
    for i in lista:
        if i[2] == cidade:
            pessoas.append(i)
    return pessoas


def pessoas_idade_maior(lista, x):
    pessoas = []
    for j in cidades(lista):
        for i in lista:
            if int(i[1]) > x and i[2] == j:
                pessoas.append(i)
    return pessoas


def pessoas_faixa(lista, x1, x2):
    pessoas = []
    for i in lista:
        if (int(i[1]) >= x1 and int(i[1]) <= x2):
            pessoas.append(i)
    return pessoas


def media_por_cidades(lista):
    idade = 0
    pessoas =0
    cidade = []
    for j in cidades(lista):
        for i in lista:
            if j == i[2]:
                idade += int(i[1])
                pessoas +=1
        media_idade = idade/pessoas
        idade = 0
        pessoas = 0
        cidade.append(f"{[j]}- {[media_idade]}")
                
    return cidade
    



dados = []
with open('pessoas.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader)
    for row in spamreader:
        dados.append(row)

print(dados)
print()
print("A")
print(pessoas_cidades(dados, "Fortaleza"))
print("B")
print(pessoas_idade_maior(dados, 30))
print("C")
print(pessoas_faixa(dados, 20, 30))
print("D")
print(media_por_cidades(dados))



