#Exercício 2

#Escreva um programa que permita ao usuário digitar 10 números quaisquer e ao final apresente o somatório e a média aritmética destes números.


soma = 0
n = 10

for i in range(n):
  num = int(input("Digite o número " + str(i + 1) + ": "))
  soma = soma + num

media = soma/n

print("A somatória é: " + str(soma), "e a média é: " + str(media))



