import numpy as np

N = 5
A = np.zeros((1,N))

for i in range(0, N-1, 1):
    if i < N:
        A[0, i] = int(input('Введите число: '))
        
print('полученный массив: ',A)

k = int(input('Введите пятое число: '))
n = int(input('Введите позицию пятого числа: '))

A[0, N-1] = k
print('Первоначальный массив: ',A)

while N > n:
    k = A[0, n-1]
    A[0, n-1] = A[0, N-1]
    A[0, N-1] = k
    n = n + 1
    
print('Массив после перестановки: ',A)    