try:
    a = input("DIgite um numero: ")
    b = input("DIgite outro numero: ")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError, ValueError):
    print("Número invalido!")
