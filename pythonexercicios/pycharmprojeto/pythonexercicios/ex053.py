frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inverso = junto[::-1]
print(' O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um polindromo!')
else:
    print('A Frase digitada não é um polindramo!')