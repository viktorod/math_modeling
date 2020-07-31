import matplotlib.pyplot as plt

def stairs(N):
    """ Функция умеет рисовать 
        лесенку, N - кол-во
        ступенек """
    x = [0]
    y = [0]
    k = 1
    
    for i in range(0, 2*N, 1):
        if i % 2 == 0:
            x.append(k-1)
            y.append(k)
        elif i % 2 == 1:
            x.append(k)
            y.append(k)
            k = k + 1
    
    plt.plot(x, y, color='k')
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.title('Stairs')
    plt.grid()
    plt.axis('equal')
    
    plt.show()
       
stairs(5)