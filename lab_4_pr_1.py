import numpy as np

N = int(input('кол-во чисел: '))

def mid(a):
   
    j=0
    for i in range(N):
       
        j=j+a[i]
    return(j/N)

a = []
a = N*[0] 

for i in range(N):
    
    a[i] = np.array(int(input('Число, пожалуйста: ')))
    
b = mid(a)

print('среднее арифм. =', b)