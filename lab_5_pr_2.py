import matplotlib.pyplot as plt
import numpy as np

def parabola (a,b,c,X,X1,N):
    """функция пытается строить параболу,
       подайте a, b и c, так же пределы и 
       кол-во точек"""
    
    x=np.linspace(X,X1,N)
    
    y=a*x**2+b*x+c
    
    plt.plot(x,y,label='y=a*x**2+b*x+c')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.title('парабола')
    plt.legend()
    
    plt.show()
    
parabola(1,0,0,-4,4,100)

def hyperbola(k, X, X1, N):
    """Функция умела строить гиперболу,
       нужно подать k, снова пределы и
       кол-во точек"""
    
    x = np.linspace(X,X1,N)
    
    y = k/x
    plt.plot(x,y,color='b', label='y = k/x')

    
    plt.title('Giperbola')
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.title('гипербола')
    plt.legend()
    plt.grid() 
    
hyperbola(1,-5,5,100)