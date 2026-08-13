#Esse programa exibi a tabela ASCII contendo os símbolos numéricos, letras maiúsculas e letras minúsculas. Com o seguinte formato:
#Símbolo – código decimal – código binário
for i in range(48,  123):
    if i < 58:
        print(f'| {chr(i)} | {i} | {bin(i) [2:]} | \n', end='') 
    elif i > 64 and i < 91:
        print(f'| {chr(i)} | {i} | {bin(i) [2:]} | \n', end='') 
    elif i > 96:
        print(f'| {chr(i)} | {i} | {bin(i) [2:]} | \n', end='') 

