
carro = float(input('Qual a velocidade que o carrou chegou? '))
multa = (carro - 80)*7
if carro >= 80:
    print(f'Você foi multado R${multa}')
else:
    print('Parabens você dirige com segurança!')
    