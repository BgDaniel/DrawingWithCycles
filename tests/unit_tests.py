from src.animate import Animator
from src.curves.circle import Circle
from src.fourier_decomposition import FourierDecompositor

coefficients = {
        -2: (-0.5, 0.4),
        -1: (1.5, 1.0),
         0: (3.0, -2.6),
        +1: (1.7, 2.0),
        +2: (-0.5, -0.9)
    }

circle = Circle(coefficients)
fourier_decompositor = FourierDecompositor(2)
fourier_coefficients = fourier_decompositor.compose(circle.curve())


def test_circle():
    print(fourier_coefficients)

#test_circle()


def test_circle_plot():
    animator = Animator(circle.curve(), fourier_coefficients)
    animator.animate()

#test_circle_plot()