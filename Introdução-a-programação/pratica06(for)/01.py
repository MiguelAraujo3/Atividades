#Os programas, a seguir, realizam a leitura do usuário de 05 (cinco) números inteiros. Ao final, exibe o último valor digitado e o maior valor lido. 
num =int(input("Digite um número: "))
qnt = 1
maior =  -9999999999999999999   
while(True):
    num = int(input("Digite um número: "))
    qnt += 1
    if num > maior:
        maior = num
    if qnt == 5:
        break
print(f'O maior número foi {maior} e o último número foi {num}')
############################################

maior = -999999999999999999999999
for i in range(0, 5):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num    
print(f'O maior número foi {maior} e o último número foi {num}')