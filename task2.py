n=int(input('сколько чисел?'))
b=0
for i in range(n):
    a=int(input('введи число'))
    if a==0:
        b+=1
if b==0:
    print('No')
else:
    print('Yes')