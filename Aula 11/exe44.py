altura =float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura + altura) 

if imc < 18.5:
    print('A baixo do peso')
elif imc <= 18.5:
     print('Peso ideal')
elif imc <= 26:
     print('Sobrepeso')
elif imc <= 31:
     print('Obesidade')
else:
     print('Obesidade mórbida')
     