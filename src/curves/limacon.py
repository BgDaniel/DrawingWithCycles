import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Limacon:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def curve(self):
        return [
            lambda t: (self._b+self._a*math.cos(2.0*math.pi*t))*math.cos(2.0*math.pi*t),
            lambda t: (self._b+self._a*math.cos(2.0*math.pi*t))*math.sin(2.0*math.pi*t)
        ]


limacon = Limacon(a=1.0, b=0.5)
fourier_decompositor = FourierDecompositor(3)
fourier_coefficients = fourier_decompositor.compose(limacon.curve(), plot=False, name="Limacon")

animator = Animator(limacon.curve(), fourier_coefficients)
animator.animate(name="Limacon, k=3")