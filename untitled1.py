import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 10)

def radio_function(n, t):
    dndt = 2*n 
    return dndt
n_0 = 1

n_b_t = odeint(radio_function, m_0, t)

plt.plot(t, n_b_t[:,0], label='Распад Урана 238')

plt.show()