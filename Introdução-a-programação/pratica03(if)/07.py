#Verificar e imprimir quantos dias tem o mês selecionado
mes = int(input("Escreva um valor correspondente a um mês do ano: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("31 dias")
elif mes == 2:
    print("28 dias")
else:
    print("30 dias")
