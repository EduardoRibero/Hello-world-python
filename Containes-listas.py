# Listas são containers que guardam dados (Objetos) em ordem.


#Uma forma de criar um lista fazia
fruit = list();

# Inserindo dados em uma lista
fruit.append("Primeio Item da Lista") 
print(fruit)

 fruit.append("Segundo Item da lista")
print(fruit)


#Outra forma de criar uma lista
fruit2 = [] 
fruit2.append("Item da lista")
print(fruit2)

#Criando já com dados
fruit3 = ["Valor1", "Valor2", "Valor3"]
print(fruit3)

#Remove o ultimo intem da lista 
intem = fruit3.pop()
print(intem)
print(fruit3)

#Juntando listas
fruitmarge = fruit3 + fruit 
print(fruitmarge)

#Verifica item na lista
tem_ou_n = "Valor1" in fruitmarge
print("Tem ou n tem é igual a: ", tem_ou_n)

#Verifica se não item na lista
tem_ou_n = "Valor45" not in fruitmarge
print("Tem ou n tem é igual a: ", tem_ou_n)

