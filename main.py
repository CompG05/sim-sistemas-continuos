import argparse

import matplotlib.pyplot as plt

from constantes import *
from funciones import *
from euler import Euler


def main():
    # Parseo de argumentos
    parser = argparse.ArgumentParser(description='Simulación de un tanque de agua', epilog='Simulación 2023')
    parser.add_argument('f_entrada', metavar='f_entrada', help='Función de entrada', type=str, choices=['constante_20', 'constante_100', 'oscilante'])
    parser.add_argument('-p', '--paso', help='Paso de simulación', type=float, default=0.1)
    parser.add_argument('-t', '--tiempo', help='Tiempo de simulación', type=float, default=200)
    parser.add_argument('-i', '--inicial', help='Valor inicial', type=float, default=1000)
    args = parser.parse_args()
    f_entrada = funciones_entrada[args.f_entrada]

    # Simulación
    e = Euler(dh, args.inicial, args.paso, f_entrada)
    valores = e.simular(args.tiempo)

    # Cálculo de entradas y salidas para graficar
    entradas = [f_entrada(0, valores[:i]) for i in range(1, len(valores))]
    salidas = [f_salida(0, v) for v in valores]
    t = [i * args.paso for i in range(len(valores))]

    # Graficar
    plt.plot(t[:], valores[:], label='h(t)')
    plt.plot(t[:], salidas[:], label='f_salida(t)')
    plt.plot(t[1:], entradas[:], label='f_entrada(t)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
