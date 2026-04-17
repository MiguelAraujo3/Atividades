#É uma competição multiesportiva que combina natação, ciclismo e corrida, realizados nessa sequência. 
#Esse programa lê o tempo (hora, minuto e segundo) de um atleta em cada uma das modalidades.
#Ao final, imprime o tempo total da prova, no formato “hora:minuto:segundo”.
#tempo natação
hn, mn, sn = input("Digite o valor do tempo da sua prova em natação de hora, minutos e segundos: ").split()
#tempo ciclismo
hci, mci, sci = input("Digite o valor do tempo da sua prova em natação de hora, minutos e segundos: ").split()
#tempo corrida
hco, mco, sco = input("Digite o valor do tempo da sua prova em natação de hora, minutos e segundos: ").split()

#todos inteiros
hn = int(hn)
hci = int(hci)
hco = int(hco)
mn = int(mn)
mci = int(mci)
mco = int(mco)
sn = int(sn)
sci = int(sci)
sco = int(sco)

#tudo em segundos
hn = hn*3600
hci = hci*3600
hco = hco*3600
mn = mn * 60
mci = mci *60
mco = mco*60

#soma de tudo
soma = hn+ mn+ sn+ hci+ mci+sci+ hco+ mco+ sco
#quantas horas totais
horas = soma//3600
#quantos minutos totais
minutos = (soma%3600)//60
#quantos segundos totais
segundos = ((soma%3600)%60)

print(f"Você demorou {horas} Horas, {minutos} Minutos, {segundos} Segundos para finalizar a competição") 




