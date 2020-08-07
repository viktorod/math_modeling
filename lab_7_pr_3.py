import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as anim    

fig, ax = plt.subplots(figsize=(10,3), facecolor='pink', frameon=True)

cycloid_line, = plt.plot([],[], color='r', label='cycloid_line')
cycloid_dot, = plt.plot([],[], 'o', color='g', label='cycloid_dot')
circle, = plt.plot([],[], color='b', label='circle')

def cycloid_func(R, t):
    """ Функция циклоиды
    """
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    
    return x, y

def circle_func(R, t):
    """ Функция круга рисующего циклоиду
    """
    alpha = np.linspace(0, 2*np.pi, 100)
    
    x = R * t + R * np.cos(alpha)
    y = R + R * np.sin(alpha)
    
    return x, y

ax.set_xlim(0,10)
ax.set_ylim(0,3)

def animate(i):
    cycloid_line.set_data(cycloid_func(R=1, t=np.linspace(0, 4*np.pi*i/100, i)))
    cycloid_dot.set_data(cycloid_func(R=1, t=4*np.pi*i/100))
    circle.set_data(circle_func(R=1, t=4*np.pi*i/100))
    
ani = anim.FuncAnimation(fig,
                         animate,
                         frames = 100,
                         interval = 10)
plt.axis('equal')
plt.legend()
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')

ani.save('lb_7_pr_3.gif')