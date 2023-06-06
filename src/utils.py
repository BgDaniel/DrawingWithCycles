import numpy as np

def get_color():
    for i in range(3):
        r = np.round(np.random.rand(), 1)
        g = np.round(np.random.rand(), 1)
        b = np.round(np.random.rand(), 1)

        return (r,g,b)
