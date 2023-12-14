# loop For:
list = ["1", "3", "2", "4"]
for show in list:
    print(show)

name = "ted"
for caracter in name:
    print(caracter)

    
# Função Range:
for i in range(1, 11):
    print(i)

for i in range(10):
    print("opa")


# loop While:
x = 10
while x > 0:
    print("{}".format(x))
    x -= 1


# Palavra chave Brak:
list = ["question 1?","question 2?","question 3?", "question 4?","question 5?","question 6?"]

n = 0

while True:
    a = input(list[n])

    if a == "q":
        break
    n = (n + 1) % 6
