import matplotlib.pyplot as plt 
import matplotlib.animation as anim 


fig, ax = plt.subplots()                                                                               


dot, = plt.plot([], [], 'o', color='k', label='dot')                  


xdata, ydata = [], []

def fractal_move(n = 50, C = 0.3, D = 0.33):
    """Функция рисует фрактал.
       На вход подаются:
       n - кол-во точек
       С и D - какие-то параметры
    """
    if n == 0:
        xdata.append(0.1)
        ydata.append(0.1)
    else:    
        xdata.append(xdata[n-1]**2 - ydata[n-1]**2 + C)
        ydata.append(2 * xdata[n-1] * ydata[n-1] + D)
    dot.set_data(xdata,ydata)
    
    return dot, 


ax.set_xlim(-0.2, 0.5)                                                                                   
ax.set_ylim(0, 0.7)

ani = anim.FuncAnimation(fig, fractal_move, frames = 300, interval = 0.1)

plt.legend()
plt.title('Фрактальное множество')
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.axis('equal')

ani.save('lab_6_pr_5.gif')
