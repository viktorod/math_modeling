import numpy as np
def func(a, b, N):
    
    x = []
    x = np.linspace(a, b, N)
    
    return (x**2)

a = int(input('что-то 1:' ))
b = int(input('что-то 2:' ))
N = int(input('что-то 3:' ))

y = func(a, b, N)
print(y)