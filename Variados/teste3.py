teste_dici = {}
nomes = []
for i in range(3):
    nome = input()
    email = input()
    teste_dici[nome] = email
    nomes.append(nome)
for i in teste_dici:
    print(teste_dici[i], end='; ')
