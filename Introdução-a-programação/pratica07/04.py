#Esse programa ler um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostra a
#sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).
m = 1
n = 1
menor = 0
maior = 0

while m > 0 and n > 0:
    soma = 0
    m, n = input("Digite um intervalo de valores: ").split()
    m = int(m)
    n = int(n)
    if m == n:
        print("Os números são igual")
    if m > n:
        menor = n
        maior = m
    else:
        menor = m
        maior = n
    for i in range(menor, maior+1):
        print(i, end=' ')
        soma += i
    print(f'Soma dos números = {soma}')












'''
m = 1
n = 1
maior = 0
while m > 0 or n > 0:
    m, n = input("Digite um intervalo de valores: ").split()
    m = int(m)
    n = int(n)
    for i in range(n, m+1):
        while n != m:
        if m > n:
            maior = n
            print(maior, end=" ")
            maior += 1
        else: 
            maior = m
            print(maior, end=' ')
            maior += 1
'''        