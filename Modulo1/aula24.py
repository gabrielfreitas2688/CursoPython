#Uso do in e not in

nome = input("Digite seu nome: ")
dado = input("Digite o que você quer encontrar: ")

if dado in nome:
    print(f"{dado} está no {nome}")

else: print(f"{dado} não está no {nome}") 