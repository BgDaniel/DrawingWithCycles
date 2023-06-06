import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Butterfly:

    def __init__(self, a):
        self._a = a

    def curve(self):
        return [
            lambda t: self._a*(-3.0*math.cos(2.0*t)+math.sin(7.0*t)-1) \
                      *math.cos(2.0*math.pi*t),
            lambda t: self._a*(-3.0*math.cos(2.0*t)+math.sin(7.0*t)-1) \
                      *math.sin(2.0*math.pi*t)
        ]


butterfly = Butterfly(a=2.0)
fourier_decompositor = FourierDecompositor(9)
fourier_coefficients = fourier_decompositor.compose(butterfly .curve(), plot=False, name="Habenicht curve")

animator = Animator(butterfly .curve(), fourier_coefficients)
animator.animate(name="Habenicht curve, k=9")