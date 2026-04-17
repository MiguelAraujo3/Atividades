#Uma empresa está com uma promoção: a cada 20 reais em compras o cliente recebe um cupom
#Esse programa recebe do usuário o valor da compra e calcula a quantidade de cupons recebido e quanto falta para receber outro cupom
#valor gasto
vg = float(input("Digite aqui o valor gasto em reais: "))
#cupons ganhos
cg = int(vg/20)
#outro cupom
oc = (20-(vg-(cg*20)))

print(f"Você ganhou {cg} cupons")
print(f"Falta {oc:.2f} reais para você ganhar outro cupom") 
