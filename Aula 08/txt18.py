import math
an = float(input('Digite o angulo que você deseja: '))
se = math.sin(math.radians(an))
print(f'O angulo de {an} tem o SENO de {se:2f} ')
cosseno = math.cos(math.radians(an))
print(f'O angulo de {an} tem a cosseno de {cosseno:2f}')
tangente = math.tan(math.radians(an))
print(f'O angulo de {an} tem a tangente de: {tangente:2f}')