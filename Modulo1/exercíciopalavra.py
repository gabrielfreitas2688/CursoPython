import os

palavra_secreta = "cachorro"
#variável está fora do while pois se tivesse dentro, seria resetada toda hora
letras_acertadas = ""
tentativas = 0

#Código inteiro dentro de um while para o jogo ficar sempre voltando para o começo

while True:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue
#Se a letra digitada estiver dentro da palavra secreta, incrementa a letra certa dentro da variável    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

#checa se a letra digitada está correta e mostra ela, caso não, mostra apenas o *
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(palavra_formada)    

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("Você acertou!")    
        print(f"A palavra secreta era {palavra_secreta}")
        print(f"Você usou {tentativas} tentativas.")
        letras_acertadas = ""
        tentativas = 0