import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as anim    

fig, ax = plt.subplots()

circle, = plt.plot([], [], color='b', label='circle')

def circle_func(r, t, x0, y0):
    """Функция надрессирована расширать окружность
    """
    alpha = np.linspace(0, 2*np.pi, 30)
    
    R = r * t 
    
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    
    return x, y

def animate(i):
    
    circle.set_data(circle_func(3, i, x0=0, y0=0))

ani = anim.FuncAnimation(fig,
                         animate,
                         frames = np.linspace(0, 2*np.pi, 100),
                         interval = 10)
plt.axis('equal')
plt.legend()
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

ani.save('lb_7_pr_2.gif')