#Exercício 1

#Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

negativos = 0

for i in range(10):
  num = int(input("Digite o número " + str(i + 1) + ": "))
  if num < 0 :
    negativos = negativos + 1

print(negativos)

