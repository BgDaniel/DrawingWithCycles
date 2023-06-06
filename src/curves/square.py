import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Square:

    def __init__(self, a=1.0):
        self._a = a

    def curve(self):

        def _x(t):
            t = t - math.floor(t)

            if 0.0 <= t and t < 1.0/8.0:
                return self._a
            elif 1.0/8.0 <= t and t < 3.0/8.0:
                return self._a/math.tan(2.0*math.pi*t)
            elif 3.0/8.0 <= t and t < 5.0/8.0:
                return - self._a
            elif 5.0/8.0 <= t and t < 7.0/8.0:
                return - self._a/math.tan(2.0*math.pi*t)
            elif 7.0/8.0 <= t and t < 1.0:
                return self._a
            else:
                raise Exception("Something went wrong!")

        def _y(t):
            t = t - math.floor(t)

            if 0.0 <= t and t < 1.0/8.0:
                return self._a*math.tan(2.0*math.pi*t)
            elif 1.0/8.0 <= t and t < 3.0/8.0:
                return self._a
            elif 3.0/8.0 <= t and t < 5.0/8.0:
                return - self._a*math.tan(2.0*math.pi*t)
            elif 5.0/8.0 <= t and t < 7.0/8.0:
                return - self._a
            elif 7.0/8.0 <= t and t < 1.0:
                return self._a*math.tan(2.0*math.pi*t)
            else:
                raise Exception("Something went wrong!")

        return [_x, _y]


square = Square()
fourier_decompositor = FourierDecompositor(15)
fourier_coefficients = fourier_decompositor.compose(square.curve(), plot=False, name="Square")

animator = Animator(square.curve(), fourier_coefficients)
animator.animate(name="Square, k=15")