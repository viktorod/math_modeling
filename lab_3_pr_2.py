import numpy as np
from scipy.constants import g

h = 100
α = np.pi / 3
β = np.pi / 6

υ = ((g * h * np.tan(β)**2) / (2 * np.cos(α)**2 * (1 - np.tan(β) * np.tan(α))))**0.5

print(υ)

from scipy.constants import k, e, h

T = 200
E = 300
N = 2 / np.pi**0.5 * h / (k * T)**(3/2) * e**(-E/(k*T)) * E**(T/2)
print('N =', N)
