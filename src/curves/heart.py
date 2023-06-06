import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Heart:

    def __init__(self, a):
        self._a = a

    def curve(self):
        return [
            lambda t: self._a*math.sin(2.0*math.pi*t)**3,
            lambda t: self._a*(13.0/16.0*math.cos(2.0*math.pi*t)-5.0/16.0*math.cos(4.0*math.pi*t) \
                      -2.0/16.0*math.cos(6.0*math.pi*t) - 1.0/16.0*math.cos(8.0*math.pi*t))
        ]


heart = Heart(a=1.0)
fourier_decompositor = FourierDecompositor(4)
fourier_coefficients = fourier_decompositor.compose(heart.curve(), plot=False, name="Heart curve")

animator = Animator(heart.curve(), fourier_coefficients)
animator.animate(name="Heart curve, k=5")