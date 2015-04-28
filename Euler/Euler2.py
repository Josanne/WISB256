'''total = 0
def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n - 2)
    
for n in range(10):
    if fib(n)<4000000:
        if fib(n) % 2 == 0:
            total += fib(n)
print(total)'''

total = 0
a = b = 1
while a < 40:
    if a % 2 == 0:
        total += a
    c = a + b
    b = a
    a = c

print(total)