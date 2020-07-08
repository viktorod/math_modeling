from scipy.constants import g
def mech_energy(m=0,h=0,v=0):
    
    E = (m * (v**2) / 2) + (m * g * h)
    return(E)

m = int(input('масса тела: '))
h = int(input('высота: '))
v = int(input('начальная скорость тела: '))

E = mech_energy(m, h, v)

print('полная механическая энергия тела =', E)