import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle

from src.helpers import get_lim, get_colors




def get_color():
    for i in range(3):
        r = np.round(np.random.rand(), 1)
        g = np.round(np.random.rand(), 1)
        b = np.round(np.random.rand(), 1)

        return (r,g,b)

class Animator:

    def __init__(self, curve, coefficients):
        self._curve = curve
        self._coefficients = coefficients
        self._colors = [get_color() for i in range(0, 2 * len(self._coefficients) + 1)]

    def animate(self, name, frames=200):
        fig, ax = plt.subplots(2, 1)
        fig.set_size_inches(16, 8)

        x_lim, y_lim = get_lim(self._curve, scale=1.5)
        ax[1].set_xlim(x_lim)
        ax[1].set_ylim(y_lim)

        self._curve_plots = []
        self._curve_plots_original = []

        self._curve_x = []
        self._curve_y = []

        dt = 1.0/float(frames)


        def _animate(i):
            circle_plots = []
            arrow_plots = []

            current_center_x, current_center_y = self._coefficients[0][0], self._coefficients[0][1]

            original_curve_x = self._curve[0](i*dt)
            original_curve_y = self._curve[1](i*dt)
            self._curve_plots_original.append(ax[1].plot(original_curve_x, original_curve_y, color="limegreen",
                                                         marker='o', markersize=1)[0])

            factors = list(self._coefficients.items())

            n = int((len(factors)-1.0)/2.0)

            rgb_1 = (0.0, 1.0, 1.0)
            rgb_2 = (1.0, 0.0, 0.0)
            colors = get_colors(2*n, rgb_1, rgb_2)
            counter = 0

            for l in range(1, n+1):
                coefficients_l = [
                    (-l, self._coefficients[-l]),
                    (+l, self._coefficients[+l]),
                ]

                for k, (alpha_k, beta_k) in coefficients_l:
                    next_center_x = current_center_x + alpha_k * math.cos(2.0 * k * math.pi * i * dt) - beta_k * math.sin(2.0 * k * math.pi * i * dt)
                    next_center_y = current_center_y + alpha_k * math.sin(2.0 * k * math.pi * i * dt) + beta_k * math.cos(2.0 * k * math.pi * i * dt)

                    r = math.sqrt(alpha_k*alpha_k+beta_k*beta_k)

                    self._set_next_plots(ax, circle_plots, arrow_plots, k, r, current_center_x, current_center_y,
                                         next_center_x, next_center_y, colors[counter])

                    current_center_x = next_center_x
                    current_center_y = next_center_y
                    counter += 1

            self._curve_x.append(current_center_x)
            self._curve_y.append(current_center_y)

            self._curve_plots.append(ax[1].plot(self._curve_x, self._curve_y, color='limegreen', linewidth=0.7)[0])

            if len(self._curve_plots) > frames:
                self._curve_plots = self._curve_plots[-frames:]

            ax[0].set_aspect('equal', 'box')
            ax[0].set_aspect('equal', 'box')
            ax[0].set_xticks(range(-n, n+1))
            ax[0].set_xlabel(r'$\omega_k$')
            ax[0].set_title(r'$r(t)=\sum_{k}\alpha_k e^{2 \pi \omega_k\sqrt{-1} t}$')
            ax[1].set_aspect('equal', 'box')
            ax[1].set_xlabel('x')
            ax[1].set_ylabel('y')

            return self._curve_plots + circle_plots + arrow_plots# + self._curve_plots_original

        anim = animation.FuncAnimation(fig, _animate, frames=frames, interval=0.5, blit=True)

        plt.legend()
        plt.suptitle(name)
        plt.show()

    def _set_next_plots(self, ax, circle_plots, arrow_plots, k, r,
                        current_center_x, current_center_y, next_center_x, next_center_y, color):

        circle = Circle((current_center_x, current_center_y), r, color=color, fill=False, linewidth=1.0)
        circle_plots.append(ax[1].add_patch(circle))

        dx = next_center_x - current_center_x
        dy = next_center_y - current_center_y
        arrow_length = math.sqrt(dx*dx+dy*dy)

        arrow_plots.append(ax[1].arrow(x=current_center_x, y=current_center_y,
                                   dx=dx,
                                   dy=dy,
                                   width=arrow_length*0.01,
                                   head_width=arrow_length*0.1,
                                   head_length=arrow_length*0.16,
                                   length_includes_head=True,
                                   color=color))

        circle = Circle((k, 0.0), r, color=color, fill=False, linewidth=1.0)
        circle_plots.append(ax[0].add_patch(circle))

        arrow_plots.append(ax[0].arrow(x=k, y=0.0,
                                   dx=dx,
                                   dy=dy,
                                   width=arrow_length*0.01,
                                   head_width=arrow_length*0.1,
                                   head_length=arrow_length*0.16,
                                   length_includes_head=True,
                                   color=color))



