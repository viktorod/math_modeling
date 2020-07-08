import numpy as np

def func(a = int(input('что-то 1:' )),
         b = int(input('что-то 2:' )),
         N = int(input('что-то 3:' ))):
    x = np.linspace(a, b, N)
    y = x ** 2
    print(y)
    return y

func()
