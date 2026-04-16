#Verificar e imprimir ao usuário se há formação de triângulo com os 3 valores lidos e qual tipo de triângulo é.
l1, l2, l3 = input("Escreve valores para os três lados de um possível triângulo: ").split()
l1 = int(l1)
l2 = int(l2)
l3 = int(l3)

if l1+l2>l3 and l2+l3>l1 and l1+l3>l2:
    print("É um triângulo")
    if l1 == l2 == l3:
        print("equilátero")
    elif l1 > l2 > l3 or l2 > l3 > l1 or l3 > l1 > l2 or l3 > l2 > l1 or l2 > l1 > l3 or l1 > l3 > l2:
        print("escaleno")
    else:
        print("isósceles")
else:
    print("Não é um triângulo")
