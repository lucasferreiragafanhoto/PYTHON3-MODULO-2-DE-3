from time import sleep
lanche = ('hamburguer', 'suco', 'pizza', 'pudim',)
# tuplas são inmutaveis
print(lanche[0:])

# referencia for cont in 2
lanche = ('hamburguer', 'suco', 'pizza', 'pudim',)
for comida in lanche:
    print(f'eu vou comer alguma {comida}')
print('comi pra caramba!')

# referencia len 3
lanche =('hamburguer','suco', 'pizza', 'pudim')
print(len(lanche))
print('comi pra caramba!')

# refrencia for cont in range 4
lanche = ('hamnúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
for cont in range(0, len(lanche)):
    print(f'eu vou comer {comida}')

print('comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')
    sleep(0.5)
print('comi pra caramba!')