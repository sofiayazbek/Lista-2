#Exercício 15

# Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 
# a) Ter no mínimo 65 anos de idade. 
# b) Ter trabalhado no mínimo 30 anos.
# c) Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 
#Com base nas informações acima, faça um algoritmo que leia: a idade e o número de anos trabalhados e imprima se ele está qualificado ou não para a aposentadoria.


idade = int(input("Digite a sua idade: "))
trab = int(input("Digite quantos anos trabalhou na empresa: "))


if (idade >= 60) and (trab >=25):
  print("Está qualificado para a aposentadoria")

elif (idade >= 65):
  print("Está qualificado para a aposentadoria")

elif (trab >=30):
  print("Está qualificado para a aposentadoria")


else:
  print("Não está qualificado para a aposentadoria")

