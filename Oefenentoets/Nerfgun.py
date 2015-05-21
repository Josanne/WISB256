import math
fv = float(input())
fz = float(input())
s = float(input())

a = float(1/2) * float(math.asin( s*fz / fv**2))

#afronden op 2 decimalen:
angle = '%.2f' % a
print(angle)