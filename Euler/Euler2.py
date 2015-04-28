total = 0
a = b = 1
while a < 4000000:
    if a % 2 == 0:
        total += a
    c = a + b
    b = a
    a = c

print(total)