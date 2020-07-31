import matplotlib.pyplot as plt 
import numpy as np

def log_spiral(b=1, title='Log_Spiral'):
    """Функция строит логарифмическую спираль. На вход подаются:
       b - необходимые параметры для создания кривой
    """      
    f = np.arange(0, 8* np.pi, 0.01)
    
    x = np.cos(f) * np.e**(b * f)
    y = np.sin(f) * np.e**(b * f)
    
    plt.plot(x, y, label='Log_Spiral', color='r')
    plt.grid()
    plt.title('логарифмическая спираль')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.axis('equal')
    
    plt.show()

log_spiral(0.2)

def arhim_spiral(k=1, title='Arhimed_Spiral'):
    """Функция строит архимедову спираль. На вход подаются:
       k - необходимые параметры для создания кривой
    """ 
    f = np.arange(0, 8* np.pi, 0.01)
    
    x = np.cos(f) * k * f
    y = np.sin(f) * k * f
    
    plt.plot(x, y, label='Arhimed_Spiral', color='g')
    
    plt.grid()
    plt.title('архимедова спираль')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.axis('equal')
    
    plt.show()
    
arhim_spiral(10)
    
def spiral_zhezl(k=1, title='Spiral_baton'):
    """Функция строит спираль-жезл. 
       На вход подаются:
       k - необходимые параметры для создания кривой
    """ 
    f = np.arange(0.01, 8* np.pi, 0.01)
    
    x = np.cos(f) * k / f**0.5
    y = np.sin(f) * k / f**0.5
    
    plt.plot(x, y, label='Spiral_Baton', color='b')
    plt.grid()
    plt.title('спираль-жезл')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.axis('equal')
    
    plt.show()

spiral_zhezl(1) 

def rosa_spiral(k=1, title='Rosa'):
    """Функция строит ну блин явно не розу.
       На вход подаются:
       k - необходимые параметры для создания кривой
    """ 
    f = np.arange(0, 8* np.pi, 0.01)
    
    x = np.cos(f) * np.sin(k * f)
    y = np.sin(f) * np.sin(k * f)

    plt.plot(x, y, label='Rosa', color='k')
    plt.grid()
    plt.title('цветок')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.axis('equal')
    
    plt.show()
    
rosa_spiral(4) 