#Exercício 4

#Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre 15 (inclusive) e 100 (inclusive).

soma = 0
contador = 0


for i in range(15,101):
  soma = soma + i
  contador = contador + 1
num = soma / contador

print("A média é: " + str(num))

# print(contador)



