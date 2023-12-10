print("Bem-vindo(a)!")
print("=============")

num_nota = int(input("Digite o número de provas realizadas: "))

soma_notas = 0

for i in range(num_nota):
    
    soma_notas += float(input(f"Digite a nota da {i + 1}: "))


media = soma_notas / num_nota 

print(f"A media das notas informadas é {media}.")
    
