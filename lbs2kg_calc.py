#! python3
# coding=utf-8
#

print('\t=============================================')
print('\t             CONVERSOR DE PESOS')
print('\t=============================================')
print('\tConversor rápido de kgs y lbs.\n\n')


lbsperkg = 2.204623

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
        print(f'\t{uni1:.2f} kg  = {uni1*lbsperkg:.2f} lbs')
        print(f'\t{uni1:.2f} lbs = {uni1/lbsperkg:.2f} kg')
input('> ')
