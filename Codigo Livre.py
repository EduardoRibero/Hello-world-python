#Codio livre

value = "777"

senha = input("Qual a senha?")

if senha == value:
    print("Beleza! Seja vem bem vindo então.")
   
    try:
         var = input("Fale um nuemero:")
         var0 = input("Fale outro nuemero:")
         var = int(var)
         var0 = int(var0)
         print(var / var0)
    except (ZeroDivisionError):
            print("Número invalido!")
    
