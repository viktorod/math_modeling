import matplotlib.pyplot as plt
x = [1,1,5,5,1]
y = [1,5,5,1,1]
plt.plot(x,y,color='k', marker='o', ms=5)
plt.xlabel('coord x')
plt.ylabel('coord y')
plt.title('square')
plt.grid()
plt.axis('equal')

plt.show()
