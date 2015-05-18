woord = list(input())
codew = list(input())
lwoord = len(woord)
lcodew = len(codew)
oplossing = ''

for i in range(lwoord):
    a = ord(woord[i])
    k = i % lcodew
    b = ord(codew[k])
    if a-b < 0:
        letter = chr(a-b + 123)
    else:
        letter = chr(a-b + 97)
    oplossing = oplossing + letter
print(oplossing)