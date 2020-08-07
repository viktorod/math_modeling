import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as anim    

fig, ax = plt.subplots(figsize=(5,8))

circle, = plt.plot([], [], color = 'r', label = 'Circle')

def circle_func(R, x0, a, b, c):
    """Функция создаёт анимацию движения окружности, 
       заданного радиуса R, 
       центр которой движется по параболе
    """
    alpha = np.linspace(0, 2 * np.pi, 100)
    
    y0 = a * x0**2 + b * x0 + c
    
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    
    return x, y

def parabola(x0, a, b, c):
    
    y0 = a * x0**2 + b * x0 + c
    
    return x0, y0

def animate(i): 
                                             
    circle.set_data(circle_func(R = 1, x0 = i, a = 1, b = -8, c = 4))

sub = parabola(x0 = np.linspace(-2, 9, 100),a = 1, b = -8, c = 4)
plt.plot(sub[0],sub[1], color = 'b', label = 'Parabola')
                 
ax.set_xlim(-1, 9)        
ax.set_ylim(-12, 4)          
plt.legend()
plt.grid()

ani = anim.FuncAnimation(fig,
                         animate,
                         frames = np.linspace(-1, 8, 100),
                         interval = 100)

ani.save('lb_7_pr_1.gif')