import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**6, 100)

def radio_function(m, t):
    dmdt = -k*m 
    return dmdt
m_0 = 10
k_Ur_238 = 4.84*10**(-18)
k_Bi_210 = 1.61*10**(-6)
k_Tl_210 = 8.76*10**(-3)

k = k_Ur_238
m_Ur_t = odeint(radio_function, m_0, t)

k = k_Bi_210
m_Bi_t = odeint(radio_function, m_0, t)

k = k_Tl_210 
m_Tl_t = odeint(radio_function, m_0, t)

plt.plot(t, m_Ur_t[:,0], label='Распад Урана 238')
plt.plot(t, m_Bi_t[:,0], label='Распад Висмута 209')
plt.plot(t, m_Tl_t[:,0], label='Распад Талия 205')

plt.show()