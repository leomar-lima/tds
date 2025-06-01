'''Questão 6
Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média.'''

from random import *

def calcular_faturamento(quantidades, precos):
    faturamentos = []
    faturamento_total = 0
    for i in range(len(quantidades)):
        faturamento = round(quantidades[i] * precos[i],2)
        faturamentos.append(faturamento)
        faturamento_total += faturamento
    
    media_faturamento = faturamento_total / len(faturamentos)
    abaixo_media = 0
    for faturamento in faturamentos:
        if faturamento < media_faturamento:
            abaixo_media += 1
            
    return faturamentos, faturamento_total, media_faturamento, abaixo_media


def main():
    quantidades = [randint(1, 100) for _ in range(20)]
    precos = [round(uniform(1, 100), 2) for _ in range(20)]
    
    faturamentos, total, media, abaixo = calcular_faturamento(quantidades, precos)

    print(f"Quantidades:{quantidades}")
    print(f"Preços: {precos}")
    print(f"Faturamentos: {faturamentos}")
    print(f"Faturamento Total: {round(total,2)}")
    print(f"Média dos Faturamentos: {round(media,2)}", )
    print(f"Número de Faturamentos abaixo da média: {abaixo}", )

if __name__ == "__main__":
    main()