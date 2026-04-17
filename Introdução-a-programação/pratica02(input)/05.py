#Esse programa lê do usuário o valor de uma determinada compra e exibir o valor a ser pago em todas as modalidades disponíveis
#inclusive o valor de cada parcela, na modalidade parcelado.
#A vista - desconto de 10%
#Cartçao de crédito - sem alteração
#Parcelado até 4x - acréscimo de 20%
#valor gasto
vg = float(input("Digite aqui o valor gasto na sua compra em reais: "))
#avista
av = vg*0.9
#cartao de credito
cc = vg
#valor parcelado
vp = (vg*1.2)
#valor de cada parcela
vcp = vp/4

print(f"À Vista o valor fica R${av:.2f}")
print(f"No cartao de crédito o valor fica R${cc:.2f}")
print(f"Parcelado o valor fica R${vp:.2f}, cada parcela sendo R${vcp:.2f}")
