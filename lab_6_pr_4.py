import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as anim

fig, ax = plt.subplots() 

line, = plt.plot([], [], color='purple')
xdata, ydata =[], []

def line_run(t):
    
    xdata.append(np.sin(t) * (np.e ** np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12) ** 5))
    
    ydata.append(np.cos(t) * (np.e ** np.cos(t) - 2 * np.cos(4*t) + np.sin(t/12) ** 5))
    
p = 5
ax.set_xlim(-p, p)
ax.set_ylim(-p, p)

def animate(i):
    
    line_run(i)
    line.set_data(xdata, ydata)
    
    return line

ani = anim.FuncAnimation(fig,
                         animate,
                         frames = np.linspace(0, 12 * np.pi, 300),
                         interval = 10)

plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.title('Бабочка')

ani.save('lb_6_pr_4_1_of_2.gif')

fig, ax = plt.subplots() 

line_2, = ax.plot([], [], color = 'r')
xdata, ydata =[], []

def line_2_run(t):
    
    xdata.append(16 * np.sin(t) ** 3)
    ydata.append(13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))

p = 20
ax.set_xlim(-p, p)
ax.set_ylim(-p, p)

def animate_part_II(i):
    line_2_run(i)
    line_2.set_data(xdata, ydata)

    return line_2
    
ani = anim.FuncAnimation(fig,
                         animate_part_II,
                         frames = np.linspace(0, 2 * np.pi, 300), 
                         interval = 10)


plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.title('Сердце')

ani.save('lb_6_pr_4_2_of_2.gif')
