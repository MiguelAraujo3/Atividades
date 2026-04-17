#Esse programa ler a quantidade de cartões amarelo e vermelho de cada jogo de cada rodada do brasileirão e mostra o somatório dos cartões por rodada.
for i in range(1, 39):
    total_amar = 0
    total_ver = 0
    for n in range(1, 11):
        amarelo = int(input(f"Digite a quantidade de cartões amarelos na rodada {i} no jogo de número {n}: "))
        vermelho = int(input(f"Digite a quantidade de cartões vermlhos na rodada {i} no jogo de número {n}: "))
        total_amar += amarelo
        total_ver += vermelho
    print(f'Foram distribuídos {total_amar} cartão(ões) amarelos e {total_ver} cartão(ões) vermelhos na rodada {i}')
