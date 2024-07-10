a = float(input('Digite a primeira reta'))
b = float(input('Digite a segundo reta'))
c = float(input('Digite a terceira reta'))

if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos acima PDEM FORMAR triangulo!')
    if a ==  b == c:
        print('Equilatero')
    if a != b != c:
        print('Escaleno')
else:
    print('Os segmentos acima NÂO podem formar um triangulo')