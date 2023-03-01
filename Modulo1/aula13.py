
#Uso do F string, possibilita usar os valores das variaveis mesmo dentro de uma string.
#Se usado como no caso do IMC, ele pode definir as casas decimais. 

nome = "Gabriel Freitas"
idade = 23
peso = 78
altura = 1.77
imc = peso / (altura*altura) 


linha_1 = f"{nome} tem {idade} anos e {peso} KG, {altura} metros e {imc:.2f} é o IMC"

print(linha_1)