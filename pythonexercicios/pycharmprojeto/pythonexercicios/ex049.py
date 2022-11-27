num = int(input('digite um número para ver sua tabuada:'))
for c in range(1, 1000):
    print('{} X {:2} = {}'.format(num, c, num*c))