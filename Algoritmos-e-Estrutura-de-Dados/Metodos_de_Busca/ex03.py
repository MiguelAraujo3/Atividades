def busca_binaria_recursiva(lista, valor, inicio, fim):
    if inicio > fim:
        return -1
    meio = (fim+inicio)//2
    if lista[meio] == valor:
        return meio
    if valor > lista[meio]:
        return busca_binaria_recursiva(lista, valor, meio+1, fim) 
    else: 
        return busca_binaria_recursiva(lista, valor, inicio, meio-1)
    
dados = [3, 5, 8, 10, 15, 17, 20]
print(busca_binaria_recursiva(dados, 17, 0, len(dados) - 1))
print(busca_binaria_recursiva(dados, 12, 0, len(dados) - 1))