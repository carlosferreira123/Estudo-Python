import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')