#Exercício 13

#Faça um algoritmo para ler as 3 notas obtidas por um aluno. Calcular a média de aproveitamento e escreva o conceito do aluno de acordo com a tabela de conceitos mais abaixo: 
# Média de Aproveitamento - Conceito
#        >= 9,0           -   A
#     >= 7,5 e < 9,0      -   B
#     >= 6,0 e < 7,5      -   C
#        < 6,0            -   D

a = float(input("Digite a primeira nota: "))
if not 0 <= a <= 10:
  raise ValueError("Entrar com valores entre 0 e 10")
b = float(input("Digite a segunda nota: "))
if not 0 <= b <= 10:
  raise ValueError("Entrar com valores entre 0 e 10")
c = float(input("Digite a terceira nota: "))
if not 0 <= c <= 10:
  raise ValueError("Entrar com valores entre 0 e 10")

med = (a+b+c)/3
media = round(med,2)

print(f"A sua média de aproveitamento é: {media}")

if media>=9.0:
  print("Conceito - A")

if 7.5<= media <9.0:
  print("Conceito - B")

if 6.0<= media <7.5:
  print("Conceito - C")

if media <6.0:
  print("Conceito - D")