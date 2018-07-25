height=eval(input('enter the value'))
row=0
for row in range(height):
    print(end=' ')
    count=0
    for count in range (height-row):
        print(end'=')
        for count in range(2*row+1):
            print(end='')
        print()
