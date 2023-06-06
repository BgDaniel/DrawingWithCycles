import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Lemniscate:

    def __init__(self, a):
        self._a = a

    def curve(self):
        return [
            lambda t: self._a*math.cos(2.0*math.pi*t)/(1.0+math.sin(2.0*math.pi*t)*math.sin(2.0*math.pi*t)),
            lambda t: self._a*math.sin(2.0*math.pi*t)*math.cos(2.0*math.pi*t)/(1.0+math.sin(2.0*math.pi*t)*math.sin(2.0*math.pi*t))
        ]


lemniscate = Lemniscate(a=1.0)
fourier_decompositor = FourierDecompositor(4)
fourier_coefficients = fourier_decompositor.compose(lemniscate.curve(), plot=False, name="Lemniscate")

animator = Animator(lemniscate.curve(), fourier_coefficients)
animator.animate(name="Lemniscate, k=5")