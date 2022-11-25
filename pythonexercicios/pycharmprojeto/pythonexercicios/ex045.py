
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('qual é sua jogada?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADO INVALIDA!')
elif computador == 1: # computador jogou papel
        if jogador == 0:
        print('computation VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
        print('JOGADOR VENCE')
        else:
            print('jOGADA INVÁLIDA!')
elif computador == 2: # COMPUTADOR JOGOU TESOURA
 if jogador == 0:
     print('JOGADOR VENCE')
 elif jogador == 1:
  print('COMPUTADOR VENCE')
 elif jogador == 2:
 else:
     print('JOGADOR ENVÁLIDA')
