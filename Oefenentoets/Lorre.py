n = int(input())
for i in range(n):
    i = input()
    count = 1
    for letter in i:
        if letter == ' ':
            count+=1
    if count <= 4:
        print(i , 'krAh!')
    else:
        print('Crackers!')
