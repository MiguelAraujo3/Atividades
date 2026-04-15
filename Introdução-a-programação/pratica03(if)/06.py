#Verificar e imprimir se 3 valores são iguais
valor1, valor2, valor3 = input("Escreva 3 valores: ").split()
valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)

if valor1 == valor2 == valor3:
    print("True")
else:
    print("False")
