from datetime import date


ano = int(input('Digite o ano que você nasceu: '))
atual = 2024 - ano

if atual <= 9:
    print(f'Você tem {atual} anos e seu nivel é Nivel mirim')
elif  atual <= 14:
    print(f'Você tem {atual} anos e seu nivel é Nivel infantil')
elif atual <= 19:
    print(f'Você tem {atual} anos e seu nivel é Junior')
elif  atual <= 25:
    print(f'Sua idade é {atual} anos e seu nivel é Senior')
else:
    print('Master')