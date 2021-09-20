#Exercício 7

#Implemente um algoritmo que imprima a sequência de fibonacci. Pergunte para o usuário quantos números, da sequência de fibonacci, ele quer que sejam impressos.
#Ex: n = 6
#1, 1, 2, 3, 5, 8


n = int(input("Quantos números, da sequência de fibonacci, deverão ser impressos? "))

t1 = 0
t2 = 1

print(f"{t2}")


for i in range (n-1):
  t3 = t1 + t2
  print(f"{t3}")
  t1 = t2
  t2 = t3  



#cont = 3
#while cont <= n:
#  t3 = t1 + t2
#  print(f"{t3}")
#  t1 = t2
#  t2 = t3
#  cont += 1


