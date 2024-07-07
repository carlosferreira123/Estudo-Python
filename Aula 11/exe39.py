from datetime import date

atual = date.today().year

ano = int(input('Diga o ano que você nasceu: '))

idade = atual - ano
 
print (f'Você tem {idade} anos em {atual}.')

if idade == 18:
   print('Você tem que se alisatar imediatamente')
elif idade < 18:
   saldo = 18 - idade
   print(f'Você ainda não tem 18 anos ainda faltam {saldo} anos para o alistamento ')
   ano = atual + saldo
   print(f'Seu alistamento será em {ano}')
elif idade > 18:
   saldo = idade - 18
   print(f'Voce já deveria ter se alistado ha {saldo} anos ')
   ano = atual - saldo
   print(f'Seu alistamento foi em {ano}')