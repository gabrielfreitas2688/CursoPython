frase = "Toda reforma interior e toda mudança para melhor dependem exclusivamente da aplicação do nosso próprio esforço."
i = 0
quant_mais = 0
letra_mais = ""


while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == " ":
        i += 1
        continue

    quant = frase.count(letra_atual)

    if quant_mais < quant:
        quant_mais = quant 
        letra_mais = letra_atual

    i += 1

print(f"A letra que apareceu mais vezes foi '{letra_mais}' e ela apareceu {quant_mais}x ")
    
    