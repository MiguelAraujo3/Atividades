#Verificar e imprimir o dia da semana a partir do número
dia = int(input("Escreva um número do dia da semana começando em 0: "))
if dia == 0:
    print("Domingo")
elif dia == 1:
    print("Segunda-feira")
elif dia == 2:
    print("Terça-feira")
elif dia == 3:
    print("Quarta-feira")
elif dia == 4:
    print("Quinta-feira")
elif dia == 5:
    print("Sexta-feira")
elif dia == 6:
    print("Sábado")
else:
    print("Não contamos como um dia da semana esse número, escreva um número válido!")
