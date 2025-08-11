# a = b mod m
a = int(input('entre com o valor de a: '))
b = int(input('entre com o valor de b: '))
m = int(input('entre com o valor do módulo: '))

resto_a = a % m
resto_b = b % m

if resto_a == resto_b:
    print(f'{a} e {b} são congruentes módulo {m}')
else:
    print(f'{a} e {b} não são congruentes módulo {m}')