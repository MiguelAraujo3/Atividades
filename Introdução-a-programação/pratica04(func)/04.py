#Esse programa vai ler valores para idade, altura, peso e salário e a partir de uma mesma função imprimir qual o maior
def maior (num1 = float, num2 = float) -> str:
    if num1 >= num2:
        return num1
    else:
        return num2
###
idade1 = int(input('Idade:'))
altura1 = float(input('Altura: '))
peso1 = float(input('Peso: '))
salario1 = float(input('Salário: '))
idade2 = int(input('Idade:'))
altura2 = float(input('Altura: '))
peso2 = float(input('Peso: '))
salario2 = float(input('Salário: '))

print(f'Maior idade: {maior(idade1, idade2) }anos')
print(f'Maior altura: {maior(altura1, altura2)} metros')
print(f'Maior peso: {maior(peso1, peso2)} kg')
print(f'Maior salário: {maior(salario1, salario2)} Reais')