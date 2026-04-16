#Verificar e imprimir qual é o maior entre 3 valores
valor1, valor2, valor3 = input("Escreva 3 valores: ").split()
valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)

if valor1>=valor2 and valor1>=valor3:
    print("O maior valor é: ", valor1)
elif valor2>=valor1 and valor2>=valor3:
    print("O maior valor é: ", valor2)
elif valor3>=valor2 and valor3>=valor1:
    print("O maior valor é: ", valor3)