import numpy as np
import math

def get_lim(curve, scale=1.0):
    l = np.linspace(0.0, 1.0, 100)
    x = [curve[0](ell) for ell in l]
    y = [curve[1](ell) for ell in l]

    return (scale*min(x), scale*max(x)), (scale*min(y), scale*max(y))

def get_colors(n, rgb_1, rgb_2):
    r = np.linspace(rgb_1[0], rgb_2[0], n)
    g = np.linspace(rgb_1[1], rgb_2[1], n)
    b = np.linspace(rgb_1[2], rgb_2[2], n)

    return [(r[i], g[i], b[i]) for i in range(n)]

def parameterize_by_arc_length(curve, n_steps=500):
    t = np.linspace(0.0, 1.0, n_steps)
    dt = 1.0/float(n_steps)
    x = [curve[0](_t) for _t in t]
    y = [curve[1](_t) for _t in t]

    dx_dt = (x[1:]-x[:-1])/dt
    dy_dt = (y[1:]-y[:-1])/dt

    s_t = [0.0]

    for _t in t:
        s_t.append(s_t[-1] + math.sqrt(dx_dt*dx_dt+dy_dt*dy_dt)*dt)

    l = s_t[-1]

    s = np.linspace(0.0, l, n_steps)

    t_s = [0.0]

    for i, _s in enumerate(s):
        j = np.abs(s_t - _s).argmin()
        t_s.append(j*dt)

    def s(t):
        return np.interp(t, s, t_s)

    return s