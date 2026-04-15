#######PROGRAMA PARA MONTAR A SEQUÊNCIA DE FIBONACCI#####
def fibonaci (value1 = int, value2 = int, n = int) -> int:
   # n = n - 1
    print(value1)
    while n > 0:
        proximo = value1 + value2
        value1=value2
        value2 = proximo
        print(value1)
        #return value1
        n -= 1

####
vezes = int(input("Escreva quantas vezes/somas você quer: "))
print(fibonaci(0, 1, vezes))