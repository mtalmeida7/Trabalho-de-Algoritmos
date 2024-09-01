contador = 0
while True:
    número = int(input('Digite um número: '))
    if número < 0:
        print(f'Foram digitados {contador} números positivos.')
        break
    else:
        contador+=1