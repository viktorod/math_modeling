import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as anim      

fig, ax = plt.subplots(figsize=(8,8)) 
            
astroid_line, = plt.plot([], [], color='r', label='astroid')
circle_inside, = plt.plot([], [], color='b', label='circle_inside')
circle_outside, = plt.plot([], [], color='b', label='circle_outside')
astroid_dot, = plt.plot([], [], 'o', color='g', label='astroid_dot') 

def astroid_func(R, t):
    """ Функция астроиды
    """
    
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
    
    return x, y

def circle_inside_func(R, t):
    """ Функция круга рисующего циклоиду
    """
    
    alpha = np.linspace(0, 2*np.pi, 100)
    
    x = 3*R/4 * np.cos(t) + R/4 * np.cos(alpha)
    y = 3*R/4 * np.sin(t) + R/4 * np.sin(alpha)
    
    return x, y

def circle_outside_func(R, t):
    """Функция статичного круга
    """
    
    alpha = np.linspace(0, 2*np.pi, 100)
    
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    
    return x, y

def animate(i):
    
    astroid_line.set_data(astroid_func(R=5, t=np.linspace(0, 4*np.pi*i/100, i)))
    astroid_dot.set_data(astroid_func(R=5, t=4*np.pi*i/100))
    circle_inside.set_data(circle_inside_func(R=5, t=4*np.pi*i/100))
    circle_outside.set_data(circle_outside_func(R=5, t=4*np.pi*i/100))

ani = anim.FuncAnimation(fig,
                         animate,
                         frames = 100,
                         interval = 10)
ax.set_xlim(-10, 10)  
ax.set_ylim(-10, 10)
plt.legend()
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')

ani.save('lb_7_pr_4.gif')