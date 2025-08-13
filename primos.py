from math import sqrt
x = int(input('entre com um valor e direi se é primo ou não: '))

lista = []

for n in range(1, x + 1):
    if x % n == 0:
        lista.append(n)

elementos_lista = len(lista)

if elementos_lista == 2:
    print(f'{x} é um número primo!')
else:
    print(f'{x} não é um número primo!')

