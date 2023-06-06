import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Habenicht:

    def __init__(self, a, n):
        self._a = a
        self._n = n

    def curve(self):
        return [
            lambda t: self._a*(1.0+math.cos(2.0*math.pi*t*self._n)+math.sin(2.0*math.pi*t*self._n)**2) \
                      *math.cos(2.0*math.pi*t),
            lambda t: self._a*(1.0+math.cos(2.0*math.pi*t*self._n)+math.sin(2.0*math.pi*t*self._n)**2) \
                      *math.sin(2.0*math.pi*t)
        ]


habenicht = Habenicht(a=2.0, n=4)
fourier_decompositor = FourierDecompositor(9)
fourier_coefficients = fourier_decompositor.compose(habenicht.curve(), plot=False, name="Habenicht curve")

animator = Animator(habenicht.curve(), fourier_coefficients)


animator.animate(name=r"Shamrock curve, $\rho(t)=1+cos(2\pi t)+sin(2\pi t)^2$, k=9")