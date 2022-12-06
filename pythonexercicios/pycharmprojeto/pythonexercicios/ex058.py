from random import  randint
computador = randint(0, 10)
print('sou o seu computador... acabei de pensar em um número entre 0 e 10.')
print('será que voçê consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... tente mais uma vez.')
        elif jogador > computador:
            print('MENOS...tente mais uma vezes.')
print('acertou com {} tentativas. parabéns!'.format(palpites))