a=int(input('введите число'))
b=a
count=1
while a!=0:
    a=int(input('введи число'))
    if a==b:
        count+=1
    elif a>b:
        b=a
        count=1
print(count)