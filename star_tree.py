def star_tree():
    height=eval(input('enter the value'))
    for row in range(height):
        for count in range(height-row):
            print(end=' ')
        for count in range(2*row+1):
            print(end='*')
        print()
