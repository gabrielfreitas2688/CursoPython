########################################################################
#Exercício 1 
########################################################################

"""numero = input("Digite um número: ")
numero_float = float(numero)

if (numero_float % 2) > 0:
    print("O número é impar!")
else:
    print("O número é par!")

if numero.isdigit():
    print("O número é inteiro!")
else: 
    print("O número não é inteiro") """

########################################################################
#Exercício 2
########################################################################
hora = input("Digite seu horário: ")

try:

    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print("Bom dia!")

    elif hora_int >= 12 and hora_int <= 17:
        print("Boa tarde!")

    elif hora_int >= 18 and hora_int <= 23:
        print("Boa noite!")

    else:
        print("Você digitou um horário incorreto!")

except:
    print("Você não digitou um número!")

""""""
########################################################################
#Exercício 3
########################################################################
"""
nome = input("Digite seu nome: ")

if len(nome) <=4:
    print("Seu nome é pequeno!")

elif len(nome) >=5 and len(nome)<= 6:
   print("Seu nome é normal!")

elif len(nome) >6:
    print("Seu nome é grande!")
else:
    print("Algo deu errado!")

"""