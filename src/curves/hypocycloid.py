import math

from src.animate import Animator
from src.fourier_decomposition import FourierDecompositor


class Hypocycloid:

    def __init__(self, r, k):
        self._r = r
        self._k = k

    def curve(self):
        return [lambda t: self._r*(self._k-1)*math.cos(2.0*math.pi*t)
                                + self._r*math.cos(2.0*(self._k-1)*math.pi*t),
                    lambda t: self._r*(self._k-1)*math.sin(2.0*math.pi*t)
                                - self._r*math.sin(2.0*(self._k-1)*math.pi*t)]


hypocycloid = Hypocycloid(r=1.0, k=3)
fourier_decompositor = FourierDecompositor(4)
fourier_coefficients = fourier_decompositor.compose(hypocycloid.curve(), plot=False, name="Hypocycloid, k=6")

animator = Animator(hypocycloid.curve(), fourier_coefficients)
animator.animate(name="Hypocycloid, k=6")