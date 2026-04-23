#Esse programa ler um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Ele apresenta a
#soma de todos os ímpares existentes entre X e Y.
i = int(input("Digite a quantiade de casos que serão testados: "))
soma = 0
for i in range(1, i+1):
    x, y = input("Digite o intervalo que serão somados os ímpares: ").split()
    x = int(x)
    y = int(y)
    soma = 0
    if x % 2 == 1 and x < y:
        x += 1
    while x != y:
        soma = 0
        if x > y:
            if x % 2 == 1:     
                soma += x
            x -= 1
        elif x < y:
            while x != y: 
                if x % 2 == 1:     
                    soma += x 
                x += 1
    print (soma)