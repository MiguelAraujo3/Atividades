#Esse programa recebe dois números inteiros e imprime -1, 1 ou 0 dependendo da relação de magnitude entre os dois valores
def analise (num1 = int, num2 = int) -> int:
    if num1 > num2:
        return -1
    elif num1 == num2:
        return 0
    else: 
        return 1
####
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
print(analise(num1, num2))