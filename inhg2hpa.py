#! python3
# coding=utf-8
#

print('\t=============================================')
print('\t         CONVERSOR DE PRESIONES')
print('\t=============================================')
print('\tConversor rápido de HPa y in Hg.\n\n')


hpaperinhg = 33.863886666667

while True:
    esnumero=True
    uni1 = input('> ')
    if uni1 == '':
        break
    for i in uni1:
        if not (i.isdigit() or (i in ',.')):
            esnumero = False
            print('Dato incorrecto. Escribe sólo números.\n')
            break
    if esnumero:
        uni1 = float(uni1)
        if uni1 < 100:
            print(f'\t{uni1:2.2f} in Hg  = {uni1*hpaperinhg:.0f} HPa')
        else:
            print(f'\t{uni1:.0f} HPa = {uni1/hpaperinhg:2.2f} in Hg')
