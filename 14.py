#Exercício 14

#Implemente um programa que apresente para o usuário se é mais vantajoso abastecer com álcool ou gasolina. Leia o valor do litro de álcool e o valor do litro de gasolina. Se o valor do litro de álcool for menor que 70% do valor do litro de gasolina, é mais vantajoso álcool, e caso contrário será mais vantajoso abastecer com gasolina.



alcool = float(input("Digite o preço do litro de álcool: "))
gasolina = float(input("Digite o preço do litro da gasolina: "))


x = 0.70*gasolina

if (alcool < x):
  print("O álcool é mais vantajoso")

else:
  print("A gasolina é mais vantajosa")

