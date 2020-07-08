from scipy.constants import g
def mech_energy(m = int(input('масса тела: ')), h = int(input('высота: ')), v = int(input('начальная скорость тела: '))):
    
    E = (m * (v**2) / 2) + (m * g * h)
    
    print('полная механическая энергия тела =', E)
    
    return(E)

E = mech_energy()
