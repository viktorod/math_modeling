a = int(input('1 число: '))
b = int(input('2 число: '))
if b == 0:
    print("на нуль делить нельзя")
elif a%b == 0:
    print("a делится на b")
    print(("Частное:" ), a//b) 
else:
    print("a не делится на b")
    print(("Остаток:"), a%b )
    print(("Частное:" ), a//b) 
