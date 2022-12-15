resp = 's'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
        resp = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    média = soma / quant
    print('voçê digitou {} números e a média foi {}'.format(quant, média))
    print('o maior valor foi {} e o menor foi {}'.format(maior, menor))