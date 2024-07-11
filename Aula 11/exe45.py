print('-----Loja do Carlos-----')


preço = float(input('Preço das compras: '))

print(''' Formas de pagamentos  
    [ 1 ] A vista dinheiro/cheque    
    [ 2 ] A vist cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço *10 /100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
     total = preço 
     parcela = total / 2
     print(f'Sua compra será parcelada em 2x de R${total} ')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra vai ser parcelada em {totparc}x de R$ {parcela}' )
else:
  total = 0   
  print('Opção invalida tente novamente')
print(f'Sua compra de {preço} vai custar {total} no final')
