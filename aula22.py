entrada = input("Você deseja anetrar no sistema? S/N ")

if entrada == "N" or entrada == "n":
  input("Você deslogou!")

senha = int(input("Digite a senha: "))
senha_correta = 12345

if (entrada == "S" or entrada == "s") and senha == senha_correta and type(senha != str):
   input("Seja bem vindo!")

else:  
    print("Senha incorreta!")



