import math

from constantes import *


def dh(t, h_ant, f_entrada):
    last_h = (1 / A) * f_entrada(t, h_ant) - (1 / A) * f_salida(t, h_ant[-1])
    return last_h


def f_entrada_oscilante(t, h_ant):
    h_max = 800
    h_min = 200
    q_max = 100
    q_min = 20
    if len(h_ant) == 1:
        return q_max

    if h_ant[-1] > h_ant[-2]:  # Si la altura está aumentando
        if h_ant[-1] >= h_max:
            return q_min
        return q_max

    # Si la altura está disminuyendo
    if h_ant[-1] <= h_min:
        return q_max
    return q_min


def f_entrada_constante_100(t, h_ant):
    return 100


def f_entrada_constante_20(t, h_ant):
    return 20


def f_salida(t, h_ant):
    return K * math.sqrt(g * h_ant)


funciones_entrada = {
    "constante_20": f_entrada_constante_20,
    "constante_100": f_entrada_constante_100,
    "oscilante": f_entrada_oscilante,
}
