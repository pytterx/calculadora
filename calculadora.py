numero1 = int(input("Numero" ))
operacao = input("sinal ")
numero2 = int(input("Numero" ))

a = numero1
b = numero2

if operacao == "+":
    soma = a + b
    print(f"{soma}")


if operacao == "-":
    sub = a - b
    print(f"{sub}")


if operacao == "*":
    mult = a * b
    print(f"{mult}")

if operacao == "/":
    div = a / b
    print(f"{div}")

