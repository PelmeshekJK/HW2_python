a = int(input('введи число'))
b = int(input('введи число'))
c = 1
while b != 0:
    while a == b and b != 0:
        d = 1
        a = b
        b = int(input('введи число'))
    d = 1
    while a < b and b != 0:
        d += 1
        if d > c:
            c = d
        a = b
        b = int(input('введи число'))
    d = 1
    while a > b and b != 0:
        d += 1
        if d > c:
            c = d
        a = b
        b = int(input('введи число'))
print(c)