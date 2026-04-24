#Este programa ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). Para cada valor lido
#imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.
#Apresenta erro se o número de entrada for negativo
x = int(input("Digite o número que você quer ver a sequência: "))
while x != 0:
    if x < 0:
        print("Erro (número negativo)")
        break
    for i in range(1, x+1):
        if i == x:
            print(i)
        else:
            print(i, end=' ')
    x = int(input("Digite o número que você quer ver a sequência: "))
   
    
    