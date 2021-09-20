#Exercício 10

#Diz a lenda que o criador do jogo de xadrez solicitou como pagamento ao rei um grão de arroz para a primeira casa do tabuleiro, dois para a segunda, quatro para a terceira, oito para a quarta, dezesseis para a quinta e assim por diante, até a sexagésima quarta casa do tabuleiro. A cada casa o valor de grãos é dobrado. Escreva um programa que calcule os seguintes valores, apresentando todos os resultados em números inteiros:

#1 Quantos grãos de arroz seriam necessários para efetuar este pagamento.

#2 Quantos quilos de arroz seriam necessários (um quilo de arroz tem aproximadamente 170 mil grãos).

#3 Quantos quilômetros quadrados seria necessário cultivar para produzir essa quantidade de arroz (um quilômetro quadrado produz aproximadamente 550 mil quilos de arroz).


#4 Quantas vezes o território brasileiro teria que ser cultivado para produzir essa quantidade de arroz (o território brasileiro tem 8.514.876 quilômetros quadrados)



n = int(input("Digite o número da casa: "))

t1 = 1
t2 = 2

#print(f"{t1}")
#print(f"{t2}")

#1
for i in range (n-2):
  t3 = t2 *2
  #print(f"{t3}")
  t1 = t2
  t2 = t3  

#2
kilo = t3/170000

#3
km = kilo/550000

#4
brasil = km/8514876


print(f"Na casa {n}, será {t3} grãos de arroz")
print(f"Seriam necessários aproximadamente {kilo} kg de arroz")
print(f"Seriam necessários aproximadamente {km} km^2")
print(f"Seriam  aproximadamente {brasil} territórios brasileiros")








