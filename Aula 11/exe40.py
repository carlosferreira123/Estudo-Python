n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media < 5.0:
    print('Aluno foi Reprovado')
elif media > 7.0:
    print('Aluno passou')
else:
    print('Recuperação')