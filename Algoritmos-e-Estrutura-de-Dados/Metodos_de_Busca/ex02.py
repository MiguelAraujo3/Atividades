def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) //2
        if lista[meio] == valor:
            resultado = meio
            while lista[resultado-1] == valor:
                resultado -=1
            return resultado
            #while lista[resultado-1] == valor:
            #    resultado -= 1
#se o valor que eu quero, é maior que o que está no meio então ele está para o "fim" da lista
        if valor > lista[meio]:
#então o inicio deve ser o primeiro indice depois do meio
            inicio = meio + 1 
#se não for quer dizer que está para o "começo" da lista
        else: 
#entao o fim tem que ser um indice antes do meio
            fim = meio - 1
        
    return None
dados = [2, 5, 5, 5, 5, 8, 11]
print(busca_binaria(dados, 5)) # 1
print(busca_binaria(dados, 7)) # None