def buscar_todos(lista, valor):
    indices = []
    for i in range(len(lista)):
        if (lista[i] == valor):
            indices.append(i)
    return indices

dados = [4, 7, 4, 9, 4]
print(buscar_todos(dados, 4)) # [0, 2, 4]
print(buscar_todos(dados, 6)) # []