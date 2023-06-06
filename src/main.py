from animate import Animator
from fourier_decomposition import FourierDecompositor
from src.curves.hypocycloid import Hypocycloid
from src.curves.square import Square

hypocycloid = Hypocycloid(a=1.0, R=2.0, r=0.5).curve()

fourier_decompositor = FourierDecompositor(10)
fourier_coefficients = fourier_decompositor.compose(hypocycloid)

animator = Animator(hypocycloid, fourier_coefficients)
#animator.animate()



square = Square(a=4.0).curve()

fourier_decompositor = FourierDecompositor(25)
fourier_coefficients = fourier_decompositor.compose(square)

animator = Animator(square, fourier_coefficients)
animator.animate()