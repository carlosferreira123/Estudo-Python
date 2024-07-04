num = int(input('Digie um numero inteiro: '))
print('''Escolha uma das opçoes:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para Binario é igual a {bin(num)}')
elif opção == 2:
    print(f'{num} convertido para octal é igual {oct(num)}') 
elif opção == 3:
     print(f'Convertido para hexadecimal é igual a {hex(num)}') 
else:
    print('Opção invalido. Tente novamnete')