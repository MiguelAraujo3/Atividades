#Esse programa mostra se um produto está apto para o consumo ou vencido, dependendo da data de validade registrada pelo usuário
from datetime import datetime

def validade (dia = int, mes = int, ano = int, valdia = int, valmes = int, valano = int) -> str:
    if ano > valano:
        return "O produto está vencido"
    elif ano < valano:
        return "O produto está apto para consumo"
    elif mes > valmes:
        return "O produto está vencido"
    elif mes < valmes:
        return "O produto está apto para o consumo"
    elif dia > valdia:
        return "O produto está vencido"
    elif dia == valdia:
        return "O produto deve ser consumido hoje"
    else: 
        return "O produto está apto para consumo"
    
agora = datetime.now()
dia = agora.day
mes = agora.month
ano = agora.year

valdia, valmes, valano = input("Escreva a data de validade do produto: ").split()
valdia = int(valdia)
valmes = int(valmes)
valano = int(valano)
print (ano)

print(validade(dia, mes, ano, valdia, valmes, valano))

