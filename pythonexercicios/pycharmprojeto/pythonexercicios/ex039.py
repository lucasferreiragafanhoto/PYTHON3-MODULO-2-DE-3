from datetime import date
atual = date . today().year
nac = int(input('qual ano de nacimento:'))
idade = atual - nac
print('quem naceu em {} tem {} anos em {}.'.format(nac, idade, atual))
if idade == 18:
    print('voçê tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('seu alistamento séra em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print(' voçê já devia ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}.'.format(ano))