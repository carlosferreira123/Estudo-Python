from random import randint
num = randint(1,5)
nu = int(input('Digite um numero de 0 a 5: '))

if nu == num:
   print(f'Parabens você acertou')
else:
   print(f'Você errou, o numero sorteado é {num}')
