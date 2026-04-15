numero = float(input("Escreva um número: "))
paridade = ""
sinal = ""
#Se o resto da divisão por 2 for 0 então ele é um número par, se não é ímpar e também diz se é maior ou menor que 0.
if numero > 0:
    sinal = "Positivo"
elif numero == 0:
    sinal = "Neutro"
else:
    sinal = "Negativo"
if numero % 2 == 0 :
    paridade = "Par"
else:
    paridade = "Ímpar"
print(f"Seu número {numero:.0f} é {sinal} e {paridade}.")
##############################################################################
#TESTE COM PORCENTAGEM
total = 100
falta = float(input("Escreva a quantidade de faltas: "))
if falta >= 0:
    presenca = total-falta
    presenca = presenca/total
    print(f"Sua taxa de presença é {presenca:.2%}")
else:
    print("ERRO")
    exit()
##############################################################################
nota = float(input("Escreva agora a sua nota: "))
if presenca >= 0.75:
    if nota >= 9:
        print("Você tirou SS!")
    elif 7 <= nota:
        print("Você tirou MS!")
    elif 5 <= nota:
        print("você tirou MM!")
    else:
        print("Você tirou MI, vai para a final")
else:
    print("Você reprovou por falta")