import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as anim

fig, ax = plt.subplots()

ball, = plt.plot( [],[], marker = 'o' , color ='r' )

def cycloid(R, t):
    
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t)) 
    
    return x, y

def animate(i):
    ball.set_data(cycloid(5, i))
    ax.set_title('Циклоида')

ani = anim.FuncAnimation(fig, animate, frames = np.arange(0, 4 * np.pi, 0.01), interval = 0.01)
c = cycloid(5, np.arange(0, 4 * np.pi, 0.01))

plt.plot(c[0], c[1], color = 'k')

plt.axis('equal')
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.grid()

ani.save('lb_6_pr_2_1_of_2.gif')

fig, ax = plt.subplots()

ball, = plt.plot( [],[], marker = 'o' , color ='r' )
    
def astroid(R, t):
    
    x = R * np.cos(t) ** 3
    y = R * np.sin(t) ** 3
    
    return x, y

def animate_part_II (i):
    ball.set_data(astroid(5, i))
    ax.set_title('Астроида')
    
ani = anim.FuncAnimation(fig, animate_part_II, frames = np.arange(0, 4 * np.pi, 0.01), interval = 100)
a = astroid(5, np.arange(0, 4 * np.pi, 0.01))
plt.plot(a[0], a[1], color = 'k')

plt.axis('equal')
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.grid()

ani.save('lb_6_pr_2_2_of_2.gif')
    
