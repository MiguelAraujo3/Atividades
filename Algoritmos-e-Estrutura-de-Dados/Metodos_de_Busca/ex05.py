import time
def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None

def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        if valor > lista[meio]:
            inicio = meio +1
        else: 
            fim = meio -1

n = 1000000
dados = list(range(n))


chave = n -1 

inicio = time.time()
indice = busca_sequencial(dados, chave)
final = time.time()
tempo = final - inicio
print(f'Sequencial: {tempo:.8f}')

# tempo busca binária
inicio = time.time()
indice = busca_binaria(dados, chave)
final = time.time()
tempo = final - inicio
print(f'Binária...: {tempo:.8f}')