viagem = float(input('Qual é a distancia da viagem em km ? '))
km = viagem * 0.50
longa = viagem * 0.45

if viagem < 200:
    print(f'A sua viagem deu R${km}')
else:
    print(f'A sua viagem deu R${longa}')