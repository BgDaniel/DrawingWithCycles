import math

from src.fourier_decomposition import FourierDecompositor


class Circle:

    def __init__(self, coefficients):
        self._coefficients = coefficients

    def curve(self):

        def _x(t):
            v = 0.0

            for k, (alpha_k, beta_k) in self._coefficients.items():
                v += alpha_k*math.cos(2.0*math.pi*k*t)-beta_k*math.sin(2.0*math.pi*k*t)

            return v

        def _y(t):
            v = 0.0

            for k, (alpha_k, beta_k) in self._coefficients.items():
                v += alpha_k*math.sin(2.0*math.pi*k*t)+beta_k*math.cos(2.0*math.pi*k*t)

            return v

        return [_x, _y]


