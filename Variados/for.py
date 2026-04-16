#Alguns programas feitos com for, para testes e aprendizado
#Contagem de 10 a 0
n = 10
for i in range(11):
    print(n)
    n -= 1

#Fatorial com for
num = int(input("Digite um número: "))
fat = 1
base = num
for i in range(num):
    fat = fat * num
    num -= 1
print(f"O fatorial do número {base} é {fat}")

#Mostrar números pares entre o intervalo de 1 e 50, código com duas formas de solução, uma está comentada
qnt = 0
for i in range(0, 51, 2):
    '''if i % 2 == 0:
        print(f'Número par: {i}')'''
    print(f'Número par: {i}')
    qnt += 1
print(f"São {qnt} números pares entre 1 e 50")

#Esse programa calcula a soma de todos os números ímpares que são múltiplos de 3 e estão no intervalo de 1 e 500, código com duas forma de solução, uma está comentada
num = 0
for i in range(3, 501, 6):
    '''if i % 2 == 1:
            if i % 3 == 0:
                num += i'''
    num += i
print(f'A soma de todos os números ímpares que são múltiplos de 3 e estão no intervalo de 1 e 500: {num}')

#Tabuada dos 11 primeiros números, de um número escolhido pelo usuário
num = int(input("Digite o número que você quer ver a tabuada: "))
mult = 0
for i in range(0, 11):
    mult = num * i
    print(f'{i} x {num} = {mult}')

#Esse progrma ler 6 números do usuário e soma apenas os valores pares, imprimindo no final esse soma
soma = 0
for i in range(1, 7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma += num
print(f'A soma dos valores pares digitados é {soma}')

#Esse programa ler o primeiro termo e a razão de uma PA e mostra os 10 primeiros termos dessa prograssão
prim = int(input("Digite o primeiro termo da PA: "))
term = prim
raz = int(input("Digite a razão dessa PA: "))
for i in range(1, 11):
    term = prim + (i - 1) * raz
    print(f'Termo {i} = {term}')

#
