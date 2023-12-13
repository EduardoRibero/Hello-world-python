# As strings assim como as listas e as tuplas são interaveis:
str = "teste"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])


# Você pode buscar strings utilizando um indice negativo
# para buscar os itens da direita para a esquerda:
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])


# Contatenação:
print(str + "nova")


# Em python é possivel multiplicar strings:
print("string " * 3)


# Para deixar um string em letras maiúsculas:
print("string maiúscula".upper())


# Para deixar um string em letras minúsculas:
print("STRING MINÚSCULA".lower())


# Deixar a primeira letra da string em maiúscula:
print("string com a primeira letra maiúscula".capitalize())


# Método Format para criar uma nova string:
print("string {}".format("Format"))


# Método Split utilizado para dividir strings apartir de um parametro:
print("17/11/2047".split("/"))


# Método Join serve para adicionar elementos entre cada caracter de uma string:
print("+".join(str))


# Também podemos transformar um lista de strings em uma unica string
# utilizando o método Join
# chmando o método em uma string vazia com a lista de parametro:
print(" ".join(["str", "string", "caracter"]))


# Podemos remover os espaços em brnaco no começo e no final de uma string
# com o metodo Strip:
print("   The   ".strip())


# Podemos substituir caracteres de um string utilizando o método Replace
# o primeiro parametro apontado é o elemento a ser substituído eo segundo substituirá:
print("07-06-2001".replace("-","/"))


# Podemos utilizar o método Index para saber o indece de algum elemento da string
# Passamos como parametro do método index o elemento que desejamos buscar
# e ele retorna o indece do da primeira ocorrencia desse elemento na string:
print("Eduardo@Ribeiro".index("@"))

# Usar as palaveas In e Not In para verificar se tem, ou não tem um certo elemento em uma string:
print("cat" in "cat in the hat")
print("cat" not in "cat in the hat")
print("bat" not in "cat in the hat")


# Usando àspas em uma string:
print("\"str\"")
print("'str'")
print('"str"')


# Pulando linhas com "\n":
print("text1ln \n text2ln \n text3ln \n text4ln")


# Fatiando uma lista:
list = ["str01","str02","str03","str04"]
print(list[0:2])
print(list[2:4])



