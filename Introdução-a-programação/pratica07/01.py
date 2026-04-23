#Esse programa tem uma variavel que vai adicionando de 3 em 3 e outra que vai subtraindo de 5 em 5, començando do 60 e essa sequência acontece até a segunda variávle chegar em 0
num2 = 60
for i in range(1, 40, 3):
    if num2 == 0:
        print(f'I={i}  J={num2}')
        num2 -= 5
        break
    else:
        print(f'I={i}  J={num2}')
        num2 -= 5