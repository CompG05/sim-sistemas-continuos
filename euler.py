from constantes import CONT_ESTAB


class Euler:
    """Clase que implementa el método de Euler para la simulación del tanque de agua."""
    def __init__(self, dq, q_0, paso, f_entrada, K):
        """Constructor de la clase.
        Args:
            - dq: función que calcula la derivada de la variable q
            - q_0: valor inicial de la variable q
            - paso: paso de la simulación
            - f_entrada: función que calcula el flujo de entrada
            - K: factor de salida
            """
        self.dq = dq
        self.q_0 = q_0
        self.paso = paso
        self.f_entrada = f_entrada
        self.y_estable = -1
        self.t_estable = -1
        self.K = K

    def simular(self, t_limite=None):
        """Simula el comportamiento del tanque de agua utilizando el método de Euler.
        Args:
            - t_limite: tiempo máximo de simulación
        Retorna una lista con los valores de la variable q en cada instante de tiempo (dependiendo del paso).
        """
        t_limit_specified = t_limite is not None
        t_limite = t_limite or float("inf")
        t = 0
        valores = [self.q_0]
        i = 0
        contador_estabilizacion = 0

        while t <= t_limite:
            t += self.paso
            # Agregar a la lista de valores el valor de q(t)
            valores.append(valores[i] + self.paso * self.dq(t, valores, self.f_entrada, self.K))
            contador_estabilizacion = contador_estabilizacion + 1 if abs(valores[i + 1] - valores[i]) < 0.01 else 0
            if contador_estabilizacion == CONT_ESTAB:
                self.t_estable = i * self.paso
                self.y_estable = valores[i + 1]
                if not t_limit_specified:
                    break

            i += 1

        return valores
