print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}->'. format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostrar a mais? '))
print('progreção finalizada com {} termos'.format(total))
