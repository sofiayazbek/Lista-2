#Exercício 12

#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. 
#Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que: 
# a) Se quantidade <= 5 o desconto será de 2% 
# b) Se quantidade > 5 e quantidade <=10 o desconto será de 3% 
# c) Se quantidade > 10 o desconto será de 5% 


nomes = input("Digite o nome do produto: ")
quants = int(input("Digite a quantidade deste produto: "))
precos = float(input("Digite o preço deste produto: "))

x = 0
y = (quants * precos)

desc1 = y*(2/100)
desc2 = y*(3/100)
desc3 = y*(5/100)


if (quants <= 5):
    x = y - desc1
if ( 5 < quants <= 10):
    x = y - desc2
if (quants > 10):
    x = y - desc3


print(f"Produto: {nomes}")
print(f"Qantidade do produto: {quants}")
print(f"Preço unitário: {precos}")

print(f"Preço total: {x}")


