#Esse programa lê o nome e o tempo de chegada (hora, minuto e segundo) de 60 atletas que participavam de um competição de 2h.
#Ao final, imprime o nome do atleta com menor tempo e o respectivo tempo.
def transform (hora = int, mim = int, sec = int) -> int:
    mim = mim + (hora * 60)
    sec = sec + (mim * 60)
    return sec
#################
nom_melh = ""
temp = 10000000
temp_melh = ""
for i in range(1, 61):
    nome, hora, mim, sec = input(f"Digite o nome do atleta número {i} e o tempo de conclusão da competição, em hora, minutos e segundos, respectivamente: ").split()
    hora = int(hora)
    mim = int(mim)
    sec = int(sec)
    if transform(hora, mim, sec) < temp:
        temp = transform(hora, mim, sec)
        nom_melh = nome
        temp_melh = (f'{hora} horas {mim} minutos e {sec} segundos')
print(f'O atleta com menor tempo foi {nom_melh} e seu tempo foi {temp_melh}')