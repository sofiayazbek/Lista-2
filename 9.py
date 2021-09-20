#Exercício 9

#Escreva um programa que imprima os n primeiros número primos. Peça para o usuário informar o valor de n.


n = int(input("Digite um número: "))


for i in range(1,n+1,1):
  primo = True
  for j in range(2,i):
    if i % j == 0 :
      primo = False
  if primo :
    print(i)





