#Sequencia de Fibonacci com For in dos 46° primeiros termos
i = int(input("Digite quantos números da sequência de Fibinacci você quer ver(até o 46° termo): "))
num1 = 0
num2 = 1
for x in range(1, i+1):
    print(num1, sep=' ', end=' ')
    proximo = num1 + num2
    num1=num2
    num2 = proximo
    if x == i:
        print(end='')
    