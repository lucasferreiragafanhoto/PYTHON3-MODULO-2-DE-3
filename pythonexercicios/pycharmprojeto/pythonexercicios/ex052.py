núm = int(input('difite um número:'))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(núm, tot))
if tot == 2:
    print('E POR ISSO ELE É PRIMO!')
else:
    print('POR ISSO ELE NÃO É PRIMO!')