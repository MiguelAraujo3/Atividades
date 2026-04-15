#Verificar e imprimir se a qual o nível de conforto a partir da temperatura
temp = float(input("Esvreva o valor da temperatura ambiente: "))
             
if temp > 30:
    print("Muito Quente")
elif temp > 26:
    print("Quente")
elif temp > 16:
    print("Agradável")
elif temp >= 10:
    print("Frio")
else: 
    print("Muito frio")
