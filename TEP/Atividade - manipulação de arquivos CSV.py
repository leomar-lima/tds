import csv

def leituta_csv(arquivo):
    with open(arquivo) as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def pessoas_cidades(lista, cidade):
    print(f'Pessoa da cidade: {cidade}')
    return [pessoa for pessoa in lista if pessoa[2] == cidade]


def pessoas_idade_maior(lista, idade):
    print(f'Pessoas com idade maior que {idade} anos:')
    return [pessoa for cidade in list(set(cidades[2] for cidades in lista)) for pessoa in lista if int(pessoa[1]) > idade and pessoa[2] == cidade]


def pessoas_faixa_etaria(lista, idade_min, idade_max):
    print(f"Faixa etaria entre {idade_min} a {idade_max} anos.")
    return [pessoa for cidade in list(set(cidades[2] for cidades in lista)) for pessoa in lista if idade_min <= int(pessoa[1]) <= idade_max and pessoa[2] == cidade]

def media_idade_por_cidades(lista):
    return {cidade: sum(int(pessoa[1]) for pessoa in lista if pessoa[2] == cidade)/sum(1 for pessoa in lista if pessoa[2] == cidade) for cidade in list(set(cidades[2] for cidades in lista))}

def main():
    arquivo = 'pessoas.csv'
    lista = leituta_csv(arquivo)

    print("Lista do arquivo CSV")
    print(lista)
    print("\na) Pessoas por cidade (ex: todos de Fortaleza).")
    print(pessoas_cidades(lista,"Fortaleza"))
    print("\nb) Pessoas com idade maior que X agrupados por cidade.")
    print(pessoas_idade_maior(lista,30))
    print("\nc) Pessoas entre faixas etárias.")
    print(pessoas_faixa_etaria(lista, 20,30))
    print("\nd) Média de idade das pessoas por cidade")
    print(media_idade_por_cidades(lista))


if __name__ == "__main__":
    main()