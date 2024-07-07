n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print(f'O {n1} é maior que {n2}.')
elif n1 == n2:
    print(f' não existe valor maior os dois são iguais')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
