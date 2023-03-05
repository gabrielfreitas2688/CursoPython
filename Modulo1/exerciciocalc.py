while True:
    
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operadores = input("Escolha um operador + - / ou * : ")
    operadores_permitidos = "-/*+"
    numerosvalidos = None

    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
     
        numerosvalidos = True
    
    except:

        numerosvalidos = None

    if numerosvalidos is None:
        print("Algum número que você digitou está errado.")
        continue

    if operadores not in operadores_permitidos:
        print("Algum operador que você digitou está errado.")
        continue
    
    if len(operadores) > 1:
        print("Digite apenas 1 operador! ")
    
    if operadores == "/" and num2_float == 0:
       print("É impossível realizar uma divisão por 0! ")
       continue

    
    print("Realizando sua conta... Confira o resultado abaixo: ")

    if operadores == "+":
        print(f"o número {num1_float} + {num2_float} é:", num2_float + num1_float)

    elif operadores == "-":
        print(f"o número {num1_float} - {num2_float} é:", num2_float - num1_float)

    elif operadores == "/":
        print(f"o número {num1_float} / {num2_float} é:", num2_float / num1_float)
   
    elif operadores == "*":
        print(f"o número {num1_float} * {num2_float} é:", num2_float * num1_float)

    else:
        print("Isso nunca deveria ter chego até aqui...")



    sair = input("Você deseja sair? [s]im ou [n]ão: ").lower().startswith('s')
    if sair:
        print("Saindo...")
        break

    
