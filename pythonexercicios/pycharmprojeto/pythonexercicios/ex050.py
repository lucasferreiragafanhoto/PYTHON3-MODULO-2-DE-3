soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite o {} valor:'.format(cont)))
    if num % 2 == 0:
        soma += num
        cont+= 1

print('voçê informou {} números pares e a soma foi {}'.format(cont, soma))
