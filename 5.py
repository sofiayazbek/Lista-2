#Exercício 5

#Escreva um programa que primeiramente peça quantos números serão digitados. Em seguida, ele deve ler cada um dos números, conforme a quantidade indicada, e ao final apresentar a média deles.

soma = 0
n = int(input("Digite quantos números serão digitados: "))

if n > 0 :

  for i in range(n):
    num = int(input("Digite os números: " + str(i + 1) + ": "))
    soma = soma + num

    media = soma/n


print("A média dos números digitados é: " + str(media))
    
