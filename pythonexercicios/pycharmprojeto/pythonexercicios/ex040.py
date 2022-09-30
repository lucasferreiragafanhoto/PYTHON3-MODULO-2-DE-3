from typing import Any

nota = float(input('primeira nota:'))
nota = float(input('segunda nota:'))
média: float | Any = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('o aunty está em Recuperação.')
elif média < 5:
    print("o aunty esta Recuperação.")
elif média >= 7:
    print('o aunty esta Aprovado.')

