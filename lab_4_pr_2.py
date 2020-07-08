import numpy as np

N = int(input('кол-во чисел: '))

def multiply(a):
   
    j=1
    for i in range(N):
       
        j=j*a[i]
    return(j)

a = []
a = N*[0] 

for i in range(N):
    
    a[i] = np.array(int(input('Число, пожалуйста: ')))
    
b = multiply(a)

print('перемножение =', b)
