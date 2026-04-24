#Esse programa verifica se o número é perfeito
x = int(input("Digite a quantidade de casos testes entre 1 e 20: "))
for i in range(1, x+1): 
    n = int(input("Digite um número: "))
    soma = 0
    num1 = 1
    while num1 < n:
        if n % num1 == 0:
            soma += num1
        num1 += 1
    if soma == n:
        print(f'O número {n} é perfeito')
    else:
        print(f'O número {n} não é perfeito')
