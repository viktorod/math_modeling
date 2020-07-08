import numpy as np
print('меню:')
print('4 стороны - прямоугольник')
print('3 стороны - треугольник,')
print('0 сторон - круг,')
def area(A = int(input('кол-во сторон:'))):
    if A == 4:
        b = int(input('сторона 1: '))
        c = int(input('сторона 2: '))
        s = b * c
    elif A == 3:
        a = int(input('длина стороны на которую упала высота: '))
        h = int(input('высота: '))
        s = 0.5 * a * h
    elif A == 0:
        r = int(input('радиус круга: '))
        s = np.pi * (r**2)
    else:
       s = print('только 0, 3 или 4 ')
    print('square = ', s)
    return(s)


area()
