import matplotlib.pyplot as plt 
import numpy as np

def cicloida(a, R):
    """Функция дрессированная на Циклоиду:(кривая, описанная точкой, лежащей на окружности радиуса R, если эта окружность катится без скольжения по прямой)
       На вход подаются:
       (t - ( https://www.kazedu.kz/referat/187764/3 ), 
       объяснение на 2 абзаце после темы)
       R - радиус окружности
    """
    if (a and R) > 0:
        
        t = np.arange(0, a * np.pi, 0.01)
    
        x = R * (t - np.sin(t))
        y = R * (1 - np.cos(t))

        plt.plot(x, y, color='k', label='Cicloida')
    
        plt.title('Cicloida')                           
        plt.xlabel('Coord - x')                         
        plt.ylabel('Coord - y')                         
        plt.axis('equal')
        plt.grid()
    
        plt.show()
        
    else:
        print('функцию я приму, но график я не дам')
    
cicloida(1, 5)

def astroida(a, R):
    """Функция дрессированная на Астроиду:(кривая, некоторой точки окружности радиуса R/4, катящейся без скольжения по другой окружности радиуса R, причем меньшая окружность все время остается внутри большей)
       На вход подаются:
       t - тожесамое что и в прошлый раз
       R - радиус окружности
    """
    
    if (a and R) > 0:
        
        t = np.linspace(0, a*np.pi, 100)
    
        x = R * np.cos(t)**3
        y = R * np.sin(t)**3

        plt.plot(x,y,color='b', label='Astroida')
    
        plt.title('Astroida')                           
        plt.xlabel('Coord - x')                         
        plt.ylabel('Coord - y')                         
        plt.axis('equal')
        plt.grid()
    
        plt.show()
    else:
        print('функцию я приму, но график я не дам')


astroida(2, 0)