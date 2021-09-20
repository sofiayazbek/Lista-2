#Exercício 8

#Implemente um algoritmo que leia um número inteiro, em seguida calcule o fatorial deste número e apresente para o usuários.
#Ex: n = 4
#O Fatorial de 4 é 24


n = int(input("Digite um número: "))

x = 1


for i in range(n,0,-1):
  x = x * i
  
print(x)








