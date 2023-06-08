class Euler:
    def __init__(self, dq, q_0, paso, f_entrada):
        self.dq = dq
        self.q_0 = q_0
        self.paso = paso
        self.f_entrada = f_entrada

    def simular(self, t_limite):
        t = 0
        valores = [self.q_0]
        i = 0

        while t <= t_limite:
            t += self.paso
            valores.append(valores[i] + self.paso * self.dq(t, valores, self.f_entrada))
            i += 1

        return valores
