termo1 = 0
termo2 = 1
numero = int(input("Digite um número inteiro positivo:"))
while termo2<numero:
    aux = termo2
    termo2 = termo2 + termo1
    termo1 = aux
if termo2 == numero:
    print("O número pertence a sequência de Fibonacci")
else:
    print("O número NÃO pertence a sequência de Fibonacci")