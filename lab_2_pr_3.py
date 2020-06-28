x = int(input('введите год: '))

if x % 4 == 0 and x % 100 != 0:
    print('год високосный')
elif x % 100 == 0 and x % 400 == 0:
    print('год високосный')
else:
    print('год не високосный') 