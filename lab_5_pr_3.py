import matplotlib.pyplot as plt 
import numpy as np

def circle(x_lim, y_lim, N, R):
    """Функция надресирована рисовать круг,
       скажите пределы, радиус, и кол-во точек
    """
    plt.xlim(-x_lim, x_lim)
    plt.ylim(-y_lim, y_lim)
    
    x = np.linspace(-2*R, 2*R, N)
    y = np.linspace(-2*R, 2*R, N)
    
    X, Y = np.meshgrid(x, y)                        
    fxy = X**2 + Y**2                               
    
    plt.contour(X, Y, fxy, levels=[R**2])           
    
    plt.grid()
    plt.title('круг')                             
    plt.xlabel('Coord - x')                         
    plt.ylabel('Coord - y')
    plt.axis('equal')  
    
    plt.show()
    
circle(10,10,1000,2)

def ellipse(x_lim, y_lim, N, a, b):
    """Тоже дресированная функция, но уже рисует 
       эллипс, дайте команду на пределы, 
       потом наградите кол-вом точек, 
       и под конец задайте a и b
    """
    plt.xlim(-x_lim, x_lim)
    plt.ylim(-y_lim, y_lim)
    
    x = np.linspace(-x_lim, x_lim, N)
    y = np.linspace(-y_lim, y_lim, N)
    
    X, Y = np.meshgrid(x, y)
    fxy = X**2 / a**2 + Y**2 / b**2
    
    plt.contour(X, Y, fxy, levels=[1]) 
    
    plt.grid()
    plt.title('эллипс')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')  
    plt.axis('equal')  
    
    plt.show()
    
ellipse(10,10,1000,7,5)