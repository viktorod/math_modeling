import numpy as np
from scipy.constants import g

h = 100
α = np.pi / 3
β = np.pi / 6

υ = ((g * h * np.tan(β)**2) / (2 * np.cos(α)**2 * (1 - np.tan(β) * np.tan(α))))**0.5

print(υ)

from scipy.constants import g, e, h, k
from math import pi
T = 200
ε = 300

N = ((2 / (pi**0.5))*(h / ((k*T)**1.5))*(e ** ((-ε) / k*T))*(ε**(T/2)))
     
print(N)