import math

from constantes import *


def dh(t, h_ant, f_entrada):
    """Función de la derivada de la altura del líquido en el tanque.
    Args:
    - t: tiempo
    - h_ant: lista de alturas anteriores
    - f_entrada: función que calcula el flujo de entrada
    """
    last_h = (1 / A) * f_entrada(t, h_ant) - (1 / A) * f_salida(t, h_ant[-1])
    return last_h


def f_entrada_oscilante(t, h_ant):
    """Función que calcula el flujo de entrada en función del tiempo.
    Causa que el líquido oscile entre 200 y 800 unidades de altura.
    Args:
    - t: tiempo
    - h_ant: lista de alturas anteriores
    """
    h_max = 800
    h_min = 200
    q_max = 100
    q_min = 20
    if len(h_ant) == 1:
        return q_max

    if h_ant[-1] > h_ant[-2]:  # Si la altura está aumentando
        if h_ant[-1] >= h_max: # Si la altura alcanzó el máximo
            return q_min       # Disminuye el flujo de entrada
        return q_max           # Si no, aumenta el flujo de entrada

                               # Si la altura está disminuyendo
    if h_ant[-1] <= h_min:     # Si la altura alcanzó el mínimo
        return q_max           # Aumenta el flujo de entrada
    return q_min               # Si no, disminuye el flujo de entrada


def f_entrada_constante_100(t, h_ant):
    """Función de entrada constante.
    Causa que la altura se estabilice por encima de 1000 unidades.
    """
    return 100


def f_entrada_constante_20(t, h_ant):
    """Función de entrada constante.
    Causa que la altura se estabilice por debajo de 200 unidades.
    """
    return 20


def f_salida(t, h_ant):
    """Función que calcula el flujo de salida en función de la altura.
    Depende de la constante K y de la altura del líquido.
    """
    return K * math.sqrt(g * h_ant)


funciones_entrada = {
    "constante_20": f_entrada_constante_20,
    "constante_100": f_entrada_constante_100,
    "oscilante": f_entrada_oscilante,
}
