#########PROGRAMA DE UMA CALCULADORA DAS 4 OPEAÇÕES
def calculadora  (valor1 = float, valor2 = float, opera = str) -> float:
    if opera == "+": 
        return valor1 + valor2
    elif opera == "-":
        return valor1 - valor2
    elif opera == "x" or opera == "*":
        return valor1 * valor2
    elif opera == "/":
        return valor1/valor2   
    else:
        return "ERRO" 
########
valor1 = float(input("Escreva um número: "))
valor2 = float(input("Escreva um número: "))
opera = input("Escreva um dos 4 sinais das operações básicas (+, -, * ou /): ")

print(f'Resultado: {calculadora(valor1, valor2, opera)}')