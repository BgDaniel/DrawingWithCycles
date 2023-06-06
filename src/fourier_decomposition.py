import math
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

class FourierDecompositor:

    def __init__(self, n):
        self._n = n

    def compose(self, curve, plot=False, name=None):
        coefficients = {}

        for k in range(-self._n, self._n+1):
            alpha_k = integrate.quad(
                lambda t: curve[0](t) * math.cos(2.0*k*math.pi*t) + curve[1](t) * math.sin(
                    2.0*k*math.pi*t), 0.0, 1.0)[0]
            beta_k = integrate.quad(
                lambda t: -curve[0](t) * math.sin(2.0 * k * math.pi * t) + curve[1](t) * math.cos(
                    2.0 * k * math.pi * t), 0.0, 1.0)[0]

            coefficients[k] = (alpha_k, beta_k)

        if plot:
            fig, ax = plt.subplots(2, 1)

            l = np.linspace(0.0, 1.0, 100)
            x = [curve[0](ell) for ell in l]
            y = [curve[1](ell) for ell in l]
            ax[0].plot(x, y, color="green")
            ax[0].set_title(name)
            ax[0].set_aspect('equal', 'box')

            k = [k for k, _ in coefficients.items()]
            alphas_k = [alpha_k for k, (alpha_k, beta_k) in coefficients.items()]
            betas_k = [beta_k for k, (alpha_k, beta_k) in coefficients.items()]

            ax[1].plot(k, alphas_k, color='red', marker='x', markersize=3, label="alpha_k",
                 linestyle="None")
            ax[1].plot(k, betas_k, color='blue', marker='o', markersize=3, label="beta_k",
                       linestyle="None")
            ax[1].legend()
            ax[1].set_title("Coefficients")
            plt.show()

        return coefficients


