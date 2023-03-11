n=int(input('введи число'))
a=1
b=1
for i in range(1, n+1):
    b=b/i
    a+=b
print(a)