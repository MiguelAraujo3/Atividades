with open ('Variados/teste.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for linha in arquivo:
        print(linha.strip().split(','))
    print(linhas)
    print(linhas)
