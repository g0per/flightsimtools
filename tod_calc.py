#! python3
# coding=utf-8
#

print('\t=============================================')
print('\t\t CALCULADORA DE APROXIMACIÓN')
print('\t=============================================')
print('\tCalculadora de descenso óptimo del 3%.\n\n\tDatos típicos: airliners -1800 fpm // GA -700 fpm.\n\n')

while True:
    while True:
        salir = False
        while True:
            alt_vuelo = input('Altitud de vuelo (ft):\t\t')
            if alt_vuelo == '':
                salir = True
                break
            elif alt_vuelo.isdigit():
                alt_vuelo = float(alt_vuelo)
                break
            else:
                print('Dato incorrecto. Escribe sólo números.\n')
        if salir:
            break

        while True:
            alt_pista = input('Altitud objetivo (ft):\t\t')
            if alt_pista == '':
                salir = True
                break
            elif alt_pista.isdigit():
                alt_pista = float(alt_pista)
                break
            else:
                print('Dato incorrecto. Escribe sólo números.\n')
        if salir:
            break

        while True:
            vel = input('Velocidad de descenso (KT):\t')
            if alt_pista == '':
                salir = True
                break
            elif vel.isdigit():
                vel = float(vel)
                break
            else:
                print('Dato incorrecto. Escribe sólo números.\n')
        if salir:
            break

        tod = ((alt_vuelo - alt_pista )*3)/1000
        rod = vel *5.2

        print( '----------------------------------------')
        print(f'\tDesciende a {rod:.0f} fpm a {tod:.0f} NM de destino.')
        print( '----------------------------------------')

    menu = input('> ')
    if menu == '':
        break
