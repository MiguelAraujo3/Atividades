#Verificar e imprimir qual têm a idade maior entre duas pessoas ditas pelo usuário
nome1, nome2 = input("Escreva o nome de duas pessoas: ").split()
idade1, idade2 = input("Escreva a idade das duas pessoas, respectivamente: ").split()
idade1=int(idade1)
idade2=int(idade2)
if idade1 > idade2:
    print(f"A pessoa mais velha é {nome1}")
elif idade2 > idade1:
    print(f"A pessoa mais velha é {nome2}")
else:
    print("Ambas tem a mesma idade")


