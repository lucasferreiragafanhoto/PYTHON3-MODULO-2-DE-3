peso = float(input('qual é o seu peso?(kg)'))
altura = float(input('qual é sua altura?(m)'))
imc = peso / altura ** 2
print(('o imc dessa pessoa é de {:.1f}'.format(imc)))
if imc < 18.5:
    print('voçê esta a baixo do peso normal')
elif 18.5 <= imc < 25:
    print('parabens , voçê esta a baixo do peso normal')
elif 25 <= imc < 30:
    print('voçê esta em Sobre peso')
elif 30 <= imc < 40:
    print('voçê esta em OBSIDADE, CUIDADO')
elif imc >= 40:
    print('voçê esta em OBESIDADE MORBIDA , CUIDADO !')