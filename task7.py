x = int(input('введи число'))
a=2
for i in range(2, int((x/2)+1)):
    if x%i==0:
        a+=1
print(a)