import matplotlib.pyplot as plt
import numpy as np

def cycloid_and_astroid(R=2):
    """ Функция строит Циклоиду и Астроиду """
    t = np.linspace(0, 2*np.pi,100)
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    
    plt.axis('equal')
    plt.plot(x,y)
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.grid()
    plt.title('cycloid')
    
    plt.show()
           
    t = np.linspace(0, 2*np.pi,100)
    
    x= R*np.cos(t)**3
    y= R*np.sin(t)**3
    
    plt.axis('equal')
    plt.plot(x,y)
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.grid()
    plt.title('astroid')

cycloid_and_astroid()
