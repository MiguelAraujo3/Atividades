def busca_sequencial(lista, valor):
    indice = None
    qnt_comp = 0 
    for i in range(len(lista)):
        qnt_comp += 1
        if lista[i] == valor:
            indice = i
            break        
    tupla = indice, qnt_comp
    return tupla

def busca_ordenada(lista, valor):
    indice = None
    qnt_comp = 0
    for i in range(len(lista)):
        qnt_comp += 1
        if lista[i] == valor:
            indice = i
            break
        qnt_comp += 1
        if lista[i] > valor:
            break
    tupla = indice, qnt_comp
    return tupla
def busca_binaria(lista, valor):
    indice = None
    qnt_comp = 0
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        qnt_comp += 1
        if lista[meio] == valor:
            indice = meio
            break
        qnt_comp += 1
        if valor > lista[meio]:
            inicio = meio + 1
        else:
            fim = meio -1
    tupla = indice, qnt_comp
    return tupla

import random
min = 1   # Limite inferior do intervalo
max = 50  # Limite superior do intervalo
tam = 20  # Tamanho da lista
dados = [random.randint(min, max) for i in range(tam)]
dados.sort()
print('Vetor:', dados)

# Gerando uma chave aleatória
chave = random.randint(min, max)
print('Chave:', chave)

# Busca Sequencial
indice, comp = busca_sequencial(dados, chave)
print(f'Busca Sequencial: {comp} comparações')

# Busca Sequencial Ordenada
indice, comp = busca_ordenada(dados, chave)
print(f'Busca Seq. Ord. : {comp} comparações')

# Busca Binária
indice, comp = busca_binaria(dados, chave)
print(f'Busca Binária   : {comp} comparações')
