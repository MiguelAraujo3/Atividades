#Esse programa simula uma compra internacional, convertendo o valor da compra de dólar para real, calculando valor do imposto de importação e o valor total
def valor_comprado (usd = float) -> float:
    brl = (usd * 5)
    return brl

def importacao (usd = float) -> float:
    importa = valor_comprado(usd)
    if importa <= 250:
        return importa * 0.20
    else:
        return importa * 0.60
    
def total (usd = float) -> float:
    total = valor_comprado(usd) + importacao(usd)
    return total

#########
valor = float(input("Escreva o valor de compra: "))
if valor < 0 :
    print("Erro, escreva um número válido")
    valor = 0
else:
    valor = valor
print(f'Valor comprado em dolár ${valor:.2f} Valor comprado em reais  R${valor_comprado(valor):.2f}, Valor da importação R${importacao(valor):.2f}, Total:  R${total(valor):.2f}')