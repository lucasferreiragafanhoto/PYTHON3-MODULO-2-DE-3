from datetime import date
atual = date . today().year
nacimento = int(input('Ano de nacimento'))
idade = atual - nacimento
print('O atleta tem {} anos'. format(idade))
if idade <= 9:
    print('classificação: Mirin')
elif idade <= 14:
    print('classificação: Infantil')
elif idade <= 14:
    print('classificação: Junior')
elif idade <= 25:
    print('classificação: Senior')
else:
    print('classificação: Master')