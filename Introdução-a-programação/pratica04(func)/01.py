#Esse programa vai exibir uma mensagem de bem vindo em português, ler dois números do usuário e imprimir a soma e o número maior
def soma(num1: int, num2: int) -> int:
    return num1 + num2
def maior (num1: int, num2: int) -> int:
    if num1 >= num2:
        return num1
    else:
        return num2
def mostrar_num (num1: int, num2: int):
    print(f'Primeiro número: {num1}')
    print(f'Segundo número: {num2}')
def mensagem_pt():
    return 'Olá, bem-vindo ao programa de operações matemáticas!'
def mensagem_en():
    return 'Hello, welcome to the math operations program!'
def idioma(idioma: str):
    if idioma == 'pt':
        msg = mensagem_pt()
    else:
        msg = mensagem_en()
    print(msg)
## programa principal
idioma('pt')
numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
mostrar_num(numero1, numero2)
x = soma (numero1, numero2)
y = maior (numero1, numero2)
print(x, y)