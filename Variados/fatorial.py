#########PROGRAMA DE NÚMEROS FATORIAIS####
def fatorial (n = int) -> int:
    num1 = n
    while n > 1:   
        n -= 1
        num1  = num1 * n
    return num1

###
valor = int(input("Escreva um número inteiro: "))
print(f'Resultado fatorial {fatorial(valor)}')