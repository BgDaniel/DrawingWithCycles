from src.curves.habenicht import Habenicht
from src.helpers import parameterize_by_arc_length
import matplotlib.pyplot as plt
import numpy as np

habenicht = Habenicht(a=2.0, n=4)
shamrock = habenicht.curve()

#s_t = parameterize_by_arc_length(shamrock)

fig, ax = plt.subplots(2, 1)

l = np.linspace(0.0, 1.0, 100)
x = [shamrock[0](ell) for ell in l]
y = [shamrock[1](ell) for ell in l]

ax[0].plot(x, y, color="green", label="original")

plt.show()



