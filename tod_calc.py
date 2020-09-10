#! python3
# coding=utf-8
#

print('\t=============================================')
print('\t\t CALCULADORA DE APROXIMACIÓN')
print('\t=============================================')
print('\n\tCalculadora de descenso óptimo del 3%.\n\tDatos típicos: airliners -1800 fpm // GA -700 fpm.\n\n')

while True:
    alt_vuelo = input('Altitud de vuelo (ft):\t\t')
    if alt_vuelo.isdigit():
        alt_vuelo = float(alt_vuelo)
        break
    else:
        print('Dato incorrecto. Escribe sólo números.\n')

while True:
    alt_pista = input('Altitud objetivo (ft):\t\t')
    if alt_pista.isdigit():
        alt_pista = float(alt_pista)
        break
    else:
        print('Dato incorrecto. Escribe sólo números.\n')

while True:
    vel = input('Velocidad de descenso (KT):\t')
    if vel.isdigit():
        vel = float(vel)
        break
    else:
        print('Dato incorrecto. Escribe sólo números.\n')

tod = ((alt_vuelo - alt_pista )*3)/1000
rod = vel *5.2

print( '----------------------------------------')
print(f'Desciende a {rod:.0f} fpm a {tod:.0f} NM de destino.\n')
input('\t[Pulsa cualquier tecla para salir]')
