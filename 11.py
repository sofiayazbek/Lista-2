#Exercício 11

#Utilizando estruturas de repetição, faça um programa que imprima a tabuada do 1 até o 10.


n = int(input("Digite um número para ver a tabuada: "))


for i in range (1, 11):
  res = n*i
  print(f"{n} X {i} = {res}")



