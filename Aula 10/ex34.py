salario = float(input('Digite seu salario: '))

if salario <= 1250:
    novo = salario + (salario *15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario} passa a ganhar R${novo}')