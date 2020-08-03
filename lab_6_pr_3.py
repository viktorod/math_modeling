import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

fig, ax = plt.subplots() 

sin_1, = plt.plot([], [], color='r')
sin_2, = plt.plot([], [], color='b')

def run_1(A, f, frame):
    
    t = np.linspace(0, frame, 100)
    y = A * np.sin(f * t) 
    
    return t, y

def run_2(A, f, frame):
    
    t = np.linspace(0, frame, 100)
    y = A * np.sin(f * t) 
    
    return t, y



def animate(i):
    
    sin_1.set_data(run_1(4, 2, i))
    sin_2.set_data(run_2(3, 1.5, i))
    
    return sin_1,sin_2

edge = 10

ax.set_xlim(0, edge)
ax.set_ylim(-edge, edge)

ani = animation.FuncAnimation(fig, 
                              animate,
                              frames = np.arange(0, 4*np.pi, 0.1),
                              interval = 0.1, blit = True)

plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.title('две синусоиды')
plt.grid()

ani.save('lb_6_pr_3.gif')
