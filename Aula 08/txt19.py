import random

n1 = input('Digite um nome: ')
n2 = input('Diite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')
lista = [n1, n2, n3, n4]
nome = random.choice(lista)
print(f'O sorteado foi {nome}')