colunas = 3
linhas = 5
matriz = [[l] * 3 for l in range(5)]

for l in range(linhas):
    print("\n")
    for c in range(colunas):
        print(matriz[l][c], end=' ')
print()
