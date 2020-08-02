import numpy as np
import matplotlib.pyplot as plt

def circle(N, R):
    """Функция надресирована рисовать круг,
       скажите радиус и кол-во точек
    """   
       
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
    
circle(1000,2)

def ellipse(x0, y0, N, a, b):
    """Тоже дресированная функция, но уже рисует 
       эллипс, дайте команду на пределы, 
       потом кол-во точек, 
       и под конец задайте a и b
    """
   
    x = np.linspace(-x0, x0, N)
    y = np.linspace(-y0, y0, N)
    
    X, Y = np.meshgrid(x, y)
    fxy = X**2 / a**2 + Y**2 / b**2
    
    plt.contour(X, Y, fxy, levels=[1])  
    
    plt.grid()
    plt.title('эллипс')                            
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')  
    plt.axis('equal')  
    
    plt.show()
    
ellipse(5,5,1000,4,2)