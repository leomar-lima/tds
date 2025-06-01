'''Questão 6
Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um
programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba
também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos
e quantos faturamentos estão abaixo da média.'''

#Utilazado 5 produtos no teste
def calcular_faturamento(quantidades, precos):
    faturamentos = []
    faturamento_total = 0
    for i in range(len(quantidades)):
        if type(quantidades[i]) != int or type(precos[i]) == str or quantidades[i] < 0 or precos[i] < 0:
            return Exception
        faturamento = round(quantidades[i] * precos[i],2)
        faturamentos.append(faturamento)
        faturamento_total += faturamento
    
    media_faturamento = faturamento_total / len(faturamentos)
    abaixo_media = 0
    for faturamento in faturamentos:
        if faturamento < media_faturamento:
            abaixo_media += 1
            
    return faturamentos, faturamento_total, media_faturamento, abaixo_media

assert calcular_faturamento([1,2,3,4,5],[1.0,2.0,3,4.5,5]) == ([1.0,4.0,9,18.0,25],57.0,11.4,3)
assert calcular_faturamento([-1,2,3,4,5],[1.0,2.0,3,4.5,5]) == Exception
assert calcular_faturamento([1,2,3,4,5],[1.0,2.0,3,-4.5,5]) == Exception
assert calcular_faturamento([" ",2,3,4,5],[1.0,2.0,3,4.5,5]) == Exception

print("TESTES OK")