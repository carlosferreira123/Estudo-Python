casa = float(input("Qual o valor da casa ? "))
salario = float(input("Qual é o seu salario ? "))
anos = int(input("Quantos anos você vai pagar ? "))

prestação = casa / (anos * 12)
minimo = salario * 30 /100
  
if prestação <= minimo:
   print(f"Emprestimo pode se concendido!")
else:
   print("Emprestimo Negado")