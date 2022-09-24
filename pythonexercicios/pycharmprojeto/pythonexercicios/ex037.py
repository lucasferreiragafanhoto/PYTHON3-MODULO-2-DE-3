num = int(input('Digite um número inteiro:'))
print(''' escolha uma das bases para conversão:
[1] converter para Binario
[2] converter para octal
[3] converter para hexadecimal ''')
opção = int(input('sua opção:'))
if opção == 1:
    print('{} convertido para Binario é igual a {}'.format( num, bin(num) [2:] ))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format( num, oct(num) [2:] ))
elif opção == 3:
     print('{} convertido para hexadecimal é igual a {}'.format( num, hex(num) [2:] ))
else:
    print('opção invalida. tente novamente.')