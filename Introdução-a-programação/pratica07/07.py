#Esse programa ler um número e imprime o fatorial dele
n = int(input("Digite um número entre 0 e 13 e eu direi seu fatorial: "))
num1 = n
x = n
if n == 0:
    num1 = 1
else:
    for i in range(1, x):
        n -= 1
        num1 = num1 * n
print (num1)