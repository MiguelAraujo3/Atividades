#Esse programa ler a quantidade de produtos avaliados por determinado consumidos. 
#Para cada produto, ler o valor antes e durante a promoção. Ao final seu programa deverá exibir:
# - Quantidade de fraudes (preço durante a promoção é igual ou superior ao preço antigo);
# - Quantidade de promoções que oferecem descontos superiores a 10%.

def promo (preco1 = float, preco2 = float) -> bool:
#preco1: preço antes da promoção; preco2: preço depois da promoção
    if preco1 > preco2:
        return True
    else:
        return False
##############
n = int(input("Digite a quantidade de produtos que serão avaliados: ")) 
qnt_fraud = 0
qnt_promo = 0
for i in range(1, n+1):
    preco1 = float(input("Digite o valor em reias antes da promoção: "))
    preco2 = float(input("Digite o valor em reais durante a promoçãp: "))
    if promo(preco1, preco2) == False:
        qnt_fraud += 1
    if preco2 < 0.9*preco1:
        qnt_promo += 1
print(f'Quantidade de fraudes obtidas {qnt_fraud}; \nQuantidade de promoções superiores a 10% obtidas: {qnt_promo}.')