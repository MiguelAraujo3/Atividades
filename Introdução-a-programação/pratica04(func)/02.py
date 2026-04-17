#Esse programa têm duas funções com conversão de unidades de temperatura, ele vai ler do usuário duas temperatura e mostrar o valor convertido
def temp_f (temp_c = float) -> float:
    temp_f = (temp_c * 9/5) + 32 
    return temp_f
def temp_k (temp_c = float) -> float:
    temp_k = temp_c + 273.15
    return temp_k
#########
temp_t = float(input("Escreve uma temperatura e vou converte-la para Fahrenheit: "))
temp_c = float(input("Escreve uma temperatura e vou converte-la para Kelvin: "))
print(f'A temperatura  {temp_t} °C convertida para Fahrenheit é {temp_f(temp_t):.2f}')
print(f'A temperatura  {temp_c} °C convertida para Kelvin é {temp_k(temp_c):.2f}')
